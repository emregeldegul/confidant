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

    @staticmethod
    def encryption(text, key):
        asciimap = lambda character: ord(character) + key
        charmap = lambda character: chr(character)
        return "".join(map(charmap, map(asciimap, list(text))))

    def save_title(self, title):
        self.title = self.encryption(title, +3)

    def show_title(self):
        return self.encryption(self.title, -3)

    def save_content(self, content):
        self.content = self.encryption(content, +3)

    def show_content(self):
        return self.encryption(self.content, -3)
