from apppkg import db  # refers to db variable __init__.py
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)

    # Note other table is capitalized.
    posts = db.relationship('Posts', backref='user', lazy=True)

    def __repr__(self):
        return f"User#{self.id} {self.user} [{self.password}]"


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Note Users table (model) isn't capitalized.Referencing 'id' column of class Users
    # Type much match type of users.id which is an integer (see Users class)
    user_fk = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # pass the callable!
    content = db.Column(db.String(150), nullable=False, default="No content")

    def __repr__(self):
        return f"{self.posted}: {self.user}"
