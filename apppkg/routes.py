from flask import render_template, flash, redirect, url_for
from apppkg import app
from apppkg.models import *
from apppkg.forms import *


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