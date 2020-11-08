from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "notsosecret"  # required for CSRF i.e. form.hidden_tag()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
db = SQLAlchemy(app)


from apppkg import routes  # not pythonic but no other solution given
