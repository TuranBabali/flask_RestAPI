import os
from decouple import config
from datetime import timedelta


BASE_DIR=os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY=True
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES= timedelta(minutes=30)
    JWT_SECRET_KEY=config('JWT_SECRET_KEY')
  


class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI='sqlite:///test.db'



class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI='sqlite:///test.db'


class ProdConfig(Config):
    pass


config_dict = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}