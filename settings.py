class BaseConfig(object):
    NNN = 123
    FILE_PATH = 'C:\\Users\\Administrator\\PycharmProjects\\File\\'
    MODEL_PATH = 'saved_models/Emotion_Voice_Detection_Model.h5'
    DB_PATH = 'mysql://root:12345678@sentiment.cepghepnnhzt.ap-northeast-1.rds.amazonaws.com:3306/sentiment'

class TestConfig(BaseConfig):
    DB = '127.0.0.1'


class DevConfig(BaseConfig):
    PATH = 'C:\\Users\\Administrator\\PycharmProjects\\File'
