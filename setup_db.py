from app import create_app
from app import db

app = create_app()
app.app_context().push()

from app.models.user import User
from app.models.diary import Diary

db.drop_all()
db.create_all()

"""
user = User(
    name = "Arne Saknussemm",
    email = "saknussemm@mail.com",
)

user.generate_password_hash('123456')

db.session.add(user)
db.session.commit()
"""
