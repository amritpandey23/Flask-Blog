from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello():
    return render_template("home.html", posts = posts, title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
    app.run(debug = True)