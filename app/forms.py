from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length
class RegistrationForm(FlaskForm):
    """
    """
    username =StringField("Username", validators = [DataRequired(), Length(min =2, max = 20,message="Username must be between 2 and 20 words" )])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators = [Length(min = 8, message = "Password must be greater than or equal to 8 ")])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign up")

class LoginForm(FlaskForm):
    """
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class QuestionsForm(FlaskForm):
    options = RadioField('Options', validators=[DataRequired()],
                        default=1)
    submit = SubmitField('Next')                       