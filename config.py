import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "A_SECRET_KEY"

    DB_NAME = "DB_NAME"
    DB_USERNAME = "DB_ADMIN"
    DB_PASSWORD = "DB_PASSWORD"

    SQLALCHEMY_DATABASE_URI = "postgresql://"+DB_USERNAME+":"+DB_PASSWORD+"@localhost:5432/"+DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    IMAGE_UPLOADS = "/home/username/app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "DB_ADMIN"
    DB_PASSWORD = "DB_PASSWORD"

    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    DB_NAME = "development-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

    SESSION_COOKIE_SECURE = False
