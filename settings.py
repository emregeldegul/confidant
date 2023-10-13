from os import getenv, path
from dotenv import find_dotenv, load_dotenv


class Settings:
    BASEDIR = path.abspath(path.dirname(__file__))

    # Get Environment Variables
    dotenv_file = find_dotenv(path.join(BASEDIR, '.env'))
    load_dotenv(dotenv_file)

    # Flask Settings
    SECRET_KEY = getenv("SECRET_KEY", "aGF5YWxpbiB5ZXJpIHlvaywgemFtYW7EsSBzYXIgZWxsZXJpbWRlbiBrYXnEsXAgZ2lkaXlvci4=")

    # APP Settings
    APP_NAME = getenv("APP_NAME", "Confidant")
    APP_DESC = getenv("APP_DESC", "Diary Software")
    APP_VERSION = getenv("APP_VERSION", "2.0.0")
    APP_DEVELOPMENT_MODE = getenv("APP_DEVELOPMENT_MODE", True)

    # Site Settings
    SITE_TITLE = getenv("SITE_TITLE", "Confidant")
    SITE_DESC = getenv("SITE_DESC", "Diary Software")
    SITE_URL = getenv("SITE_URL", "http://127.0.0.1:5000")

    # Author Settings
    AUTHOR_NAME = getenv("AUTHOR_NAME", "Yunus Emre Geldegül")
    AUTHOR_EMAIL = getenv("AUTHOR_EMAIL", "yunusemregeldegul@gmail.com")
    AUTHOR_SITE_URL = getenv("AUTHOR_SITE_URL", "https://emregeldegul.com.tr")

    # SQLAlchemy Database Settings
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///" + path.join(BASEDIR, "confidant.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)


settings = Settings()
