from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import forms


app = Flask(__name__)
app.config["SECRET_KEY"] = "notsosecret"  # required for CSRF i.e. form.hidden_tag()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
db = SQLAlchemy(app)

class Agenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False, default="None")

    def __repr__(self):
        return self.id


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    return render_template("contact.html")


@app.route("/register", methods=['POST', 'GET'])
def register():
    f = forms.RegistrationFm()

    if f.validate_on_submit():
        flash(f"An account has been created for {f.username.data}", 'success')  # second arg captures bootstrap result success
        return redirect(url_for('index'))

    return render_template("register.html", title="Register", form=f)


@app.route("/login", methods=['POST', 'GET'])
def login():
    f = forms.LoginFm()
    return render_template("login.html", title="Login", form=f)


if __name__ == "__main__":
    app.run(debug=True)
