from flask import render_template, flash, redirect, url_for
from apppkg import app, db, bcrypt
from apppkg.models import *
from apppkg.forms import *
from flask_login import login_user


@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("index.html")


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    return render_template("contact.html")


@app.route("/register", methods=['POST', 'GET'])
def register():
    f = RegistrationFm()

    if f.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(f.password.data).decode('utf-8')
        new_user = Users(user=f.user.data, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash(f"Account created for {f.user.data}", 'success')
        return redirect(url_for('login'))

    return render_template("register.html", title="Register", form=f)


@app.route("/login", methods=['POST', 'GET'])
def login():
    f = LoginFm()

    if f.validate_on_submit():
        logging_user = Users.query.filter_by(user=f.user.data).first()

        if logging_user and bcrypt.check_password_hash(logging_user.password, f.password.data):
            login_user(logging_user, remember=f.remember.data)  # remember takes a boolean
            return redirect(url_for('home'))
        else:
            flash(f"Unsuccessful login for {f.user.data}!", 'danger')  
    return render_template("login.html", title="Login", form=f)
