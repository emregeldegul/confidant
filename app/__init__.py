from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please Login'
    login_manager.login_message_category = 'info'

    from app.routes.auth import auth
    app.register_blueprint(auth)

    from app.routes.main import main
    app.register_blueprint(main)

    from app.routes.diary import diary
    app.register_blueprint(diary)

    from app.routes.profile import profile
    app.register_blueprint(profile)

    return app
