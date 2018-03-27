import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hard to guess string'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
        
    MAIL_USERNAME = 'chengengwei01@163.com'
    MAIL_PASSWORD = 'wei5726854'
    FLASKY_MAIL_SUBJECT_PREFIX = '[JeaDong]'
    FLASKY_MAIL_SENDER = 'chengengwei01@163.com'
    FLASKY_ADMIN = 'chengengwei01@163.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False#不懂
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True#每次提交结果自动保持到数据库
    @staticmethod
    def init_app(app):#对配置环境初始化
        pass


class DevelopmentConfig(Config):
    DEBUG = True#打开调试模式
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
