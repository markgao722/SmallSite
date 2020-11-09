from apppkg import db, login_manager  # refers to variables in  __init__.py
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    user_id = int(user_id)
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):
    # Check the table by importing Users from the terminal, then run a query Users.query.first()
    # Users.query.all() -> list of objects representing users (username and hashed passwords shown)
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)

    # Note other table is capitalized.
    posts = db.relationship('Posts', backref='user', lazy=True)

    def __repr__(self):
        return f"User#{self.id} {self.user} [{self.password}]"


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Note Users table (model) isn't capitalized. Referencing 'id' column of class Users
    # Type much match type of users.id which is an integer (see Users class)
    user_fk = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # pass the callable!
    content = db.Column(db.String(150), nullable=False, default="No content")

    def __repr__(self):
        return f"{self.posted}: {self.user}"
