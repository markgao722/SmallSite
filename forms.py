from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp


class RegistrationFm(FlaskForm):
    # all elements of the form are attributes of a Flaskform class
    user = StringField("Username", validators=[
        DataRequired(),
        Length(min=2, max=20),
        Regexp("[A-z]+|[0-9]+[0-9]|[A-z]")  # PasswordField has builtin RE but anonymizes text input
    ])

    password = StringField("Password", validators=[
        DataRequired(),
        Length(min=3, max=50),
    ])

    password_confirm = StringField("Confirm Password", validators=[
        DataRequired(),
        EqualTo("Password")
    ])

    submit_btn = SubmitField("Register")

class LoginFm(FlaskForm):
    user = StringField("Username", validators=[
        DataRequired(),
        Length(min=2, max=30),
    ])

    password = PasswordField("Password", validators=[
        DataRequired(),
    ])

    remember = BooleanField("Remember Me")
    submit_btn = SubmitField("Log In")
