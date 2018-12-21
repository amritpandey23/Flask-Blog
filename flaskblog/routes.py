from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
# We have used flask_bcrypt to encrypt user password.
from flask_bcrypt import Bcrypt
from flaskblog import db
from flask_login import login_user, logout_user, current_user

bcrypt = Bcrypt()

posts = [
    {
        "author" : "Amrit Pandey",
        "title" : "First ever blog post",
        "content" : "Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero ipsam ipsum repellendus distinctio illo ipsa voluptatum voluptatibus eaque dolorum incidunt quasi obcaecati dolores, corrupti, amet, necessitatibus blanditiis? Nisi, a aliquid.",
        "date_posted" : "April 20, 2018"
    },
    {
        "author" : "Janet Doe",
        "title" : "Second ever blog post",
        "content" : "Lorem ipsum dolor sit amet coFirstnsectetur adipisicing elit. Libero ipsam ipsum repellendus distinctio illo ipsa voluptatum voluptatibus eaque dolorum incidunt quasi obcaecati dolores, corrupti, amet, necessitatibus blanditiis? Nisi, a aliquid.",
        "date_posted" : "April 21, 2018"
    }
]


### HOME ROUTE ###
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts = posts, title="Home")


### ABOUT PAGE ROUTE ###
@app.route("/about")
def about():
    return render_template("about.html", title="About")


### REGISTRATION FORM AND ROUTE ###
@app.route("/register", methods=["GET", "POST"])
def register():

    # if user is already logged in:
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Store the form model in a variable so that it is handy to use.
    form = RegistrationForm()

    # Validate the form as user submit it and also display a flash message
    # on the top of content block if the forms validates or returns errors.
    if form.validate_on_submit():
        # Commit the details filled by end-user to database.
        user = User(username=form.username.data, email=form.email.data, password=bcrypt.generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()

        # FLASH MESSAGE DISPLAY ON TOP
        # To create a flash message pass two arguments:
        #   - message
        #   - category(for css styling purposes): success, error, warning etc.
        flash(f"Account created for {form.username.data}!", category="success")
        # REDIRECT TO HOMEPAGE ON VALIDATION
        return redirect(url_for('home'))
    
    # If the form is not submited just simply render the register form.
    return render_template("register.html", title="Register", form=form)


### LOGIN FORM AND ROUTE ###
@app.route("/login", methods=["GET", "POST"])
def login():

    # if user is already logged in:
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Store form model in a variable so that it is handy
    form = LoginForm()

    # When user have submitted the login form and is validated
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # Send this user data to login manager to handle login session
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash(f"Login unsuccessful, Check email or password!", category="danger")

    # Render the login form when page loads
    return render_template("login.html", title="login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))