from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
db = SQLAlchemy(app)

class Agenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False, default="None")

    def __repr__(self):
        return self.id


@app.route("/", methods=['POST', 'GET',])
def index():
    return render_template("index.html")

app.run(debug=True)
