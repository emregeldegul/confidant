from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from settings import settings

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please login to access this page."
    login_manager.login_message_category = "info"

    # Inıt Routes
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    from app.routes.diary import diary_bp
    app.register_blueprint(diary_bp)

    from app.routes.profile import profile_bp
    app.register_blueprint(profile_bp)

    return app
