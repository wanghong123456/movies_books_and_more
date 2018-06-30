import os

base_path = os.path.abspath(os.path.dirname(__file__))

# The base class of all environments


class Config:
    SECRET_KEY = 'books_and_movies_and_more'
    # The configurations of the databases
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

# The configurations of development


class DevelopConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://develop:project123@127.0.0.1:3306/development'

# The configurations of productions


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://develop:project123@127.0.0.1:3306/production'


config = {
    'default': DevelopConfig,
    'production': ProductionConfig,
}
