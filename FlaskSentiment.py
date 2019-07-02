import os
import random
import time
import json
import EmotionClassify
from flask import Flask, current_app, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy

ALLOWED_EXTENSIONS = set(['mp3', 'wav'])
loaded_model = None

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/semtiment"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
# app.config.from_object('settings.BaseConfig')
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

    def __repr__(self):
        return '<AudioRecords %s %s %s %s %s %s>' % (self.record_id, self.record_name, self.record_date, self.type_id,
                                                     self.customer_id, self.employee_id)


@app.route('/')
def audio_records():
    # customer = Customer.query.filter(Customer.customer_id == 2).first()
    # key = "".join(random.choice("0123456789") for i in range(8))
    # print(current_app.config['PATH'])
    audio_record = AudioRecords.query.all()
    entries = [dict(record_id=row.record_id, record_name=row.record_name, record_date=str(row.record_date),
                    type=row.type_id, employee_id=row.employee_id,
                    customer_id=row.customer_id) for row in audio_record]
    result = EmotionClassify.getEmotions('TestAudio/test_4.wav')
    # print(result)
    for re in result:
        start_time = re[0]
        end_time = re[1]
        status = re[2]
        sr = StatusRecords(record_id=1, start_time=start_time, end_time=end_time, status=status)
        db.session.add(sr)
        db.session.commit()
    # return render_template('audio_records.html', entries=entries)
    return json.dumps(entries)


@app.route('/add_records')
def add_records():
    business = BusinessType.query.all()
    types = [dict(type_id=row.type_id, type_name=row.type_name, parent_type=row.parent_type) for row in business]
    return render_template('add_records.html', types=types)


@app.route('/upload_records', methods=['POST', 'GET'])
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
            db.session.commit()
            return redirect(url_for('audio_records'))
        else:
            error = 'Invalid File Type'
    return render_template('add_records.html', error=error)


@app.route('/analysis', methods=['POST', 'GET'])
def analysis():
    error = None
    record_id = request.form['record_id']
    record_name = request.form['record_name']
    record_date = request.form['record_date']
    type = request.form['type']
    employee_id = request.form['employee_id']
    customer_id = request.form['customer_id']
    return "audio_records" + record_id


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# def auto_analysis(filename):



if __name__ == '__main__':
    EmotionClassify.loadModel(current_app.config['MODEL_PATH'])
    app.run(debug=True)

