from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager
from app.models.abstract import BaseModel


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()


class User(BaseModel, UserMixin):
    __tablename__ = "users"  # noqa

    full_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(70), nullable=False, unique=True)
    password_hash = db.Column(db.String(94), nullable=False)
    birthday = db.Column(db.Date, nullable=True)

    def generate_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password_hash):
        return check_password_hash(self.password_hash, password_hash)
