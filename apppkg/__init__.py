from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "notsosecret"  # required for CSRF i.e. form.hidden_tag()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
db = SQLAlchemy(app)
# db.create_all()

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from apppkg import routes  # not pythonic but no other solution given
