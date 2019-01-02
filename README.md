## Installation 
*You'll need python3.6 or above, use your version of python instead of 3.7 in procedures below.*
1. Clone and move into directory `git clone https://gitlab.com/amritpandey/flask-blog-2.git && cd flask-blog-2`
2. Setup virtual environment `python3.7 -m venv venv`
3. Install dependencies `pip3 install requirements.txt`
4. For now, we have to initialise db, so open up python repl and import db `from flaskblog import db` and initialise by `db.create_all()`.
5. Finally, run the project `python run.py` or `flask run` by exporting flaskblog to FLASK_APP in terminal `export FLASK_APP=flaskblog`.

## Stack Developer Docs
1. Flask: http://flask.pocoo.org/docs/1.0/
2. Jinja2: http://jinja.pocoo.org/docs/2.10/
3. Sqllite3: https://docs.python.org/2/library/sqlite3.html

## Package Structure
```
.
├── flaskblog
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   └── main.css
│   └── templates
│       ├── about.html
│       ├── account.html
│       ├── home.html
│       ├── layout.html
│       ├── login.html
│       └── register.html
├── run.py
```