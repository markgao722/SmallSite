from flask import Flask, render_template, flash, redirect, url_for
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
        flash(f"An account has been created for {f.user.data}", 'success')  # second arg captures bootstrap result success
        print("redirect")
        return redirect(url_for('index'))

    return render_template("register.html", title="Register", form=f)


@app.route("/login", methods=['POST', 'GET'])
def login():
    f = forms.LoginFm()

    if f.validate_on_submit():
        if f.user.data == "god" and f.password.data == "123":
            flash(f"Successful login in God Mode. Maximum admin priviledges granteed.", 'success')  
            return redirect(url_for('index'))    
        else:
            flash(f"Successful login test for {f.user.data}!", 'success')  
            return redirect(url_for('index'))
    return render_template("login.html", title="Login", form=f)


if __name__ == "__main__":
    app.run(debug=True)
