from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, ValidationError
from apppkg.models import Users

class RegistrationFm(FlaskForm):
    # all elements of the form are attributes of a Flaskform class
    user = StringField("Username", validators=[
        DataRequired(),
        Length(min=1, max=20),
    ])

    password = StringField("Password", validators=[
        DataRequired(),
        Length(min=3, max=50),
    ])

    password_confirm = StringField("Confirm Password", validators=[
        DataRequired(),
        EqualTo("password")
    ])

    submit_btn = SubmitField("Register")


    def validate_username(self, username):
        check = Users.query.filter_by(user=username.data).first()
        if check:
            raise ValidationError("This username already exists.")

    def validate_username(self, password):
        check = Users.query.filter_by(password=password.data).first()
        if check:
            raise ValidationError("This Password already exists.")


class LoginFm(FlaskForm):
    user = StringField("Username", validators=[
        DataRequired(),
        Length(min=1, max=20),
    ])

    password = PasswordField("Password", validators=[
        DataRequired(),
        Length(min=3, max=50),
    ])

    remember = BooleanField("Remember Me")
    submit_btn = SubmitField("Log In")
