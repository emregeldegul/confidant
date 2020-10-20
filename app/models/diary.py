from app import db

class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='user')
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(70), nullable=False, unique=True)
    date = db.Column(db.Date, nullable=False)

    def __str__(self):
        return "<Diary: {}: {} ({})>".format(self.user.name, self.title, self.date)
