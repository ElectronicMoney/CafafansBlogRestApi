from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField(
        'Username:', 
        validators=[DataRequired(), Length(min=6, max=20)]
    )

    email = StringField(
        'Email:', 
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        'Password:', 
        validators=[DataRequired(),  Length(min=6, max=20)]
    )

    confirm_password = PasswordField(
        'Confirm Password:', 
        validators=[DataRequired(),  EqualTo('password')]
    )

    submit = SubmitField('Sign Up')