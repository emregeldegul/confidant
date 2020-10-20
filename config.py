from os import getenv, path, urandom
from dotenv import load_dotenv

class Config():
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, '.env'))

    SECRET_KEY = getenv('SECRET_KEY') or urandom(24)
    PORT = getenv('PORT') or 80
    DEBUG = getenv('DEBUG') or False
    TESTING = getenv('TESTING') or False
    ENV = getenv('ENV') or 'production'
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + path.join(basedir, 'confidant.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
