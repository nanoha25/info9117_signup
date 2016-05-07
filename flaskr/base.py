#all imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

#more imports
from contextlib import closing

#configuration
DATABASE = '/tmp/flaskr.db' #this is a path useable only on *nix system. Using this path under Windows will cause error.
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#create our little application :)

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode = 'r') as f: #"f" stands for the name of an object created through app.open_resource
            db.cursor().executescript(f.read()) #f.read() stands for an action which reads info from object with the name "f"
        db.commit()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

