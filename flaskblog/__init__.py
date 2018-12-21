from flask import Flask
# SQLAlchemy is an ORM(Object Relational Mapping) 
# https://en.wikipedia.org/wiki/Object-relational_mapping
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Anything that requires encryption (for safe-keeping against 
# tampering by attackers) requires the secret key to be set.
app.config["SECRET_KEY"] = "aaa269055db1c78ee6d59ef9"

# The database URI that should be used for the connection
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# Create database
db = SQLAlchemy(app)

login_manager = LoginManager()

from flaskblog import routes