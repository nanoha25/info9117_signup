#all imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flaskr import base

app = Flask(__name__)
app.config.from_object(__name__)



def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/contact', methods=['POST'])
def add_entry():
    g.db.execute('insert into entries (title, text, email) values (?, ?, ?)',[request.form['title'], request.form['text'], request.form['email']])
    g.db.commit()
    flash('Your enquiry has been sent!')
    return redirect(url_for('contactform'))

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

