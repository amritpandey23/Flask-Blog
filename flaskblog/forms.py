# Flask data models that will store data submitted by users
# through forms can easily be created with flask_wtf package
# and FlaskForm module. These also help in rendering the
# form HTML.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

# REGISTRATION FORM MODEL
class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    # We first need to check whether the details submitted by the
    # end user is unique to the data we already have. For eg.
    # `username` and `email` should be unique to each user, if
    # not the sqlite will throw an error.

    # Two functions have been defined to cross check if same
    # `username` or `email` exist as entered by end-user.

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f"'{user.username}' is already taken, please use another!")
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(f"'{user.email}' already exist, please use another!")


# LOGIN FORM MODEL
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")
