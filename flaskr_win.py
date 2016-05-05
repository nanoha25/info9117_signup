#all imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

#more imports
from contextlib import closing

#configuration
DATABASE = '/tmp/flaskr.db' # this is a path useable only on *nix system. Using this path under Windows will cause error.
DATABASE_WIN = "flaskr.db" # just use relative path and let python to handle everythine else. So problem avoided.
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#create our little application :)

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def connect_db_win():
    return sqlite3.connect(app.config['DATABASE_WIN'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode = 'r') as f: #"f" stands for the name of an object created through app.open_resource
            db.cursor().executescript(f.read()) #f.read() stands for an action which reads info from object with the name "f"
        db.commit()

def init_db():
    with closing(connect_db_win()) as db:
        with app.open_resource('schema.sql', mode = 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

#tutorial step 4

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

