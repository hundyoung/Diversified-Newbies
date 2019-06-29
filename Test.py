import librosa.display
import numpy as np
from keras.models import model_from_json
import pandas as pd
import librosa
from sklearn.preprocessing import LabelEncoder
from pydub import AudioSegment
from pydub.silence import split_on_silence

def splitAudio(audio_path):
    sound = AudioSegment.from_mp3(audio_path)
    # loudness = sound.dBFS
    # print(loudness)

    chunks = split_on_silence(sound,
                              # must be silent for at least three a second,
                              min_silence_len=3000,

                              # consider it silent if quieter than -16 dBFS
                              silence_thresh=-16,
                              keep_silence=500

                              )
    print('The number of segments：', len(chunks))

    # Abandon the segments whose length < 3s
    index=0
    fileStr = audio_path.split('.')

    for i in list(range(len(chunks)))[::-1]:
        if len(chunks[i]) >= 3000 and len(chunks[i]) <= 10000:
            chunks[i].export(fileStr[0]+"_"+str(index)+"."+fileStr[1],bitrate='192k', format="wav")
            index+=1

    print('The number of valid segments：', index)
    return index
    # return chunks

def loadModel(model_path):
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights(model_path)
    print("Loaded model from disk")
    return loaded_model

def classifyEmotion(path,loaded_model):
    lb = LabelEncoder()
    feeling_list=['female_angry','female_calm','female_fearful','female_happy','female_sad','male_angry','male_calm','male_fearful','male_happy','male_sad']
    labels = pd.DataFrame(feeling_list)
    lb.fit_transform(labels)

    X, sample_rate = librosa.load(path, res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)
    sample_rate = np.array(sample_rate)
    livedf2 = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13),axis=0)
    # featurelive = mfccs
    # livedf2 = featurelive
    livedf2= pd.DataFrame(data=livedf2)
    livedf2 = livedf2.stack().to_frame().T
    twodim= np.expand_dims(livedf2, axis=2)
    livepreds = loaded_model.predict(twodim,
                             batch_size=32,
                             verbose=1)
    livepreds1=livepreds.argmax(axis=1)
    liveabc = livepreds1.astype(int).flatten()
    livepredictions = (lb.inverse_transform((liveabc)))
    return livepredictions[0]

audio_path = 'output10.wav'
index = splitAudio(audio_path)
fileStr = audio_path.split('.')

loaded_model = loadModel(model_path="saved_models/Emotion_Voice_Detection_Model.h5")
# print(classifyEmotion(path=audio_path,loaded_model=loaded_model))
for i in range(index):
    print(classifyEmotion(path=fileStr[0]+"_"+str(i)+"."+fileStr[1],loaded_model=loaded_model))
# print(liveabc)