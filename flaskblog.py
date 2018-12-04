from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "aaa269055db1c78ee6d59ef9"

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

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts = posts, title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="login", form=form)

if __name__ == "__main__":
    app.run(debug = True)