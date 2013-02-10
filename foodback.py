from __future__ import with_statement
from contextlib import closing

import sqlite3
from flask import (Flask, request, session, g, redirect, url_for, abort,
        render_template, flash)

# configuration
# TODO Put in separate file, production/development configs, etc.
DATABASE = '/tmp/foodback.db'
DEBUG = True

# Create application
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    cur = g.db.execute('select name from serveries order by id')
    entries = [dict(title=row[0]) for row in cur.fetchall()]
    # TODO: do this right
    content = render_template('index.html', entries=entries)
    return render_template('default.html', content=content)

@app.route("/student")
def student():
    # TODO: do this right
    content = render_template('student.html')
    return render_template('default.html', content=content)

@app.route("/chef")
def chef():
    # TODO: do this right
    content = render_template('chef.html')
    return render_template('default.html', content=content)

@app.route("/ratings/<servery>")
def ratings(servery):
    # TODO: translate urls into valid serverys and invalid serverys
    servery = servery.title()
    # TODO: do this right
    content = render_template('ratings.html', servery=servery)
    return render_template('default.html', content=content)

### DATABASE STUFF
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
            db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

### VIEW STUFF
@app.route('/login', methods=['GET', 'POST'])
def login():
    # TODO CAS...
    pass

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
