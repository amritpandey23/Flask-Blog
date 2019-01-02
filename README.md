## Installation  
1. Clone it https://gitlab.com/amritpandey/flask-blog-2.git
2. Install virtual environment `python -m venv venv`
3. Install all the dependencies `pip install requirements.txt`
4. Run the project `python flaskblog.py` or `flask run` by exporting flaskblog.py to FLASK_APP in terminal.

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