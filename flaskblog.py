from flask import Flask, render_template, url_for, flash, redirect
# SQLAlchemy is an ORM(Object Relational Mapping) 
# https://en.wikipedia.org/wiki/Object-relational_mapping
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import DataTime

app = Flask(__name__)

# Anything that requires encryption (for safe-keeping against 
# tampering by attackers) requires the secret key to be set.
app.config["SECRET_KEY"] = "aaa269055db1c78ee6d59ef9"

# The database URI that should be used for the connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# Create database
db = SQLAlchemy(app)

# Table for User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)
    # __repr__ is a built-in function used to compute 
    # the "official" string reputation of an object.
    def __repr__():
        return f"User: ('{self.username}', '{self.email}', '{self.image_file}')"

# Table for Post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=DataTime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    def __repr__():
        return f"Post: ('{self.title', '{self.date_posted}')"

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
    # Store the form model in a variable so that it is handy to use.
    form = RegistrationForm()

    # Validate the form as user submit it and also display a flash message
    # on the top of content block if the forms validates or returns errors.
    if form.validate_on_submit():
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
    form = LoginForm()
    return render_template("login.html", title="login", form=form)


# Every module in python has a special attribute called __name__ .
# The value of __name__  attribute is set to '__main__'  when 
# module run as current program. Otherwise the value of __name__  
# is set to contain the name of the module which is currently running.
if __name__ == "__main__":
    app.run(debug = True)