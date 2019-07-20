import os
import random
import time
import json
import EmotionClassify
from flask import Flask, current_app, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy

ALLOWED_EXTENSIONS = set(['mp3', 'wav'])
loaded_model = None
negative_emotions = ['female_angry', 'female_fearful', 'female_sad', 'male_angry',
                     'male_fearful', 'male_sad']
calm = ['female_calm', 'male_calm']
positive_emotions = ['female_happy', 'male_happy']
app = Flask(__name__)
# app.config.from_object('settings.BaseConfig') loaded in __init__
# UPLOAD_FOLDER = current_app.config['PATH']
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)


class Customer(db.Model):
    __tablename__ = 'customer'
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50))

    def __repr__(self):
        return '<Customer %s>' % self.customer_name


class BusinessType(db.Model):
    __tablename__ = 'businesstype'
    type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(50))
    parent_type = db.Column(db.String(50))

    def __repr__(self):
        return '<BusinessType %s %s %s>' % (self.type_id, self.type_name, self.parent_type)


class StatusRecords(db.Model):
    __tablename__ = 'statusrecords'
    status_id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.String(10))
    start_time = db.Column(db.Integer)
    end_time = db.Column(db.Integer)
    status = db.Column(db.String(30))

    def __repr__(self):
        return '<StatusRecords %s %s %s %s %s>' % (self.status_id, self.record_id, self.start_time,
                                                   self.end_time, self.status)


class AudioRecords(db.Model):
    __tablename__ = 'audiorecords'
    record_id = db.Column(db.Integer, primary_key=True)
    record_name = db.Column(db.String(50))
    record_date = db.Column(db.DateTime)
    type_id = db.Column(db.Integer)
    customer_id = db.Column(db.Integer)
    employee_id = db.Column(db.Integer)
    result = db.Column(db.Integer)

    def __repr__(self):
        return '<AudioRecords %s %s %s %s %s %s %s>' % (self.record_id, self.record_name, self.record_date, self.type_id,
                                                     self.customer_id, self.employee_id,self.result)


@app.route('/audio_records')
def audio_records():
    audio_record = AudioRecords.query.all()
    entries = [dict(record_id=row.record_id, record_name=row.record_name, record_date=str(row.record_date),
                    type=row.type_id, employee_id=row.employee_id,
                    customer_id=row.customer_id,overall_evaluation= row.result) for row in audio_record]
    # return render_template('audio_records.html', entries=entries)
    return json.dumps(entries), 200, [("access-Control-Allow-Origin", "*")]


@app.route('/audio_details')
def audio_details():
    # record_id = request.args.get('record_id') check if the parm is submitted with form
    record_id = request.args.get('record_id')
    audio_record = AudioRecords.query.get(record_id)
    status_record = StatusRecords.query.filter_by(record_id=record_id).all()
    entries = {'record_id': audio_record.record_id, 'record_name': audio_record.record_name,
                'record_date': str(audio_record.record_date), 'type': audio_record.type_id,
                'employee_id': audio_record.employee_id, 'customer_id': audio_record.customer_id,'overall_evaluation': audio_record.result,
                'analyzer_result': [dict(start_time=row.start_time, end_time=row.end_time, status=row.status)
                                    for row in status_record]}
    # return render_template('audio_records.html', entries=entries)
    print(json.dumps(entries))
    return json.dumps(entries), 200, [("access-Control-Allow-Origin", "*")]


@app.route('/add_records')
def add_records():
    business = BusinessType.query.all()
    types = [dict(type_id=row.type_id, type_name=row.type_name, parent_type=row.parent_type) for row in business]
    # return render_template('add_records.html', types=types)
    return json.dumps(types), 200, [("access-Control-Allow-Origin", "*")]


@app.route('/upload_records', methods=['POST', 'GET', 'OPTIONS'])
def upload_records():
    error = None
    file = request.files['file']
    if request.method == 'POST':
        if file and allowed_file(file.filename):
            customer_id = request.form['customer_id']
            employee_id = request.form['employee_id']
            type_id = request.form['type']
            timekey = time.strftime("%Y%m%d", time.localtime())
            key = "".join(random.choice("0123456789") for i in range(8))
            suf = file.filename.rsplit('.', 1)[1]
            filename = timekey + '_' + key + '.' + suf
            file.save(os.path.join(current_app.config['FILE_PATH'], filename))
            ar = AudioRecords(record_name=filename, record_date=timekey, type_id=int(type_id),
                              customer_id=int(customer_id), employee_id=int(employee_id))
            db.session.add(ar)
            db.session.flush()
            record_id = ar.record_id
            db.session.commit()
            auto_analysis(record_id, filename)
            # return redirect(url_for('audio_records'))
        else:
            error = 'Invalid File Type'
    return 'Hello World!', 200,  [("access-Control-Allow-Origin", "*")]


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def auto_analysis(record_id, filename):
    results = EmotionClassify.getEmotions(current_app.config['FILE_PATH'] + filename)
    total_length = results[-1][1]
    first_section_end = total_length // 3
    last_section_start = first_section_end * 2
    first_vote_dict = {}
    last_vote_dict = {}
    for re in results:
        start_time = re[0]
        end_time = re[1]
        status = re[2]
        sr = StatusRecords(record_id=record_id, start_time=start_time, end_time=end_time, status=status)
        db.session.add(sr)
        db.session.commit()
        if end_time <= first_section_end:
            first_vote_dict[status] = first_vote_dict.get(status, 0) + (end_time - start_time)
        elif first_section_end < end_time and first_section_end >= start_time:
            first_vote_dict[status] = first_vote_dict.get(status, 0) + (first_section_end - start_time)
        if start_time >= last_section_start:
            last_vote_dict[status] = last_vote_dict.get(status, 0) + (end_time - start_time)
        elif last_section_start > start_time and last_section_start <= end_time:
            last_vote_dict[status] = last_vote_dict.get(status, 0) + (end_time - last_section_start)
    first_section_emotion = labelEmotion(max(first_vote_dict, key=first_vote_dict.get))
    last_section_emotion = labelEmotion(max(last_vote_dict, key=last_vote_dict.get))
    result = last_section_emotion-first_section_emotion
    # audio_record = AudioRecords.query.filter(record_id == record_id).first()
    # audio_record.result = result
    AudioRecords.query.filter_by(record_id=record_id).update({'result': result})

    db.session.commit()

def labelEmotion(emotion):
    if emotion in positive_emotions:
        return 1
    elif emotion in calm:
        return 0
    elif emotion in negative_emotions:
        return -1

if __name__ == '__main__':
    app.config.from_object('settings.BaseConfig')
    model_path = app.config['MODEL_PATH']
    DB_PATH = app.config['DB_PATH']
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_ECHO'] = True
    EmotionClassify.loadModel(model_path=model_path)
    app.run()

