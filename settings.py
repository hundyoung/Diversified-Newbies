class BaseConfig(object):
    NNN = 123
    FILE_PATH = 'C:\\Users\\Administrator\\PycharmProjects\\File'
    MODEL_PATH = 'saved_models/Emotion_Voice_Detection_Model.h5'

class TestConfig(BaseConfig):
    DB = '127.0.0.1'


class DevConfig(BaseConfig):
    PATH = 'C:\\Users\\Administrator\\PycharmProjects\\File'
