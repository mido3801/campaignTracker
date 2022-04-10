#api/config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {'host': 'localhost',
                        'db': 'test',
                        'port': 27017,
                        'username': 'useradmin',
                        'password': 'password'}


env_config = {'development': DevConfig}
