from __future__ import with_statement
import urllib
from contextlib import closing

import sqlite3
from flask import (Flask, request, session, g, redirect, url_for, abort,
        render_template, flash)
import pycas

# configuration
# TODO Put in separate file, production/development configs, etc.
DATABASE = '/tmp/foodback.db'
DEBUG = True
SECRET_KEY = "This is a very secret key. No one must know!"

CAS_SERVER = "https://netid.rice.edu"
# TODO url_for
SERVICE_URL = "http://localhost:5000"

# Create application
app = Flask(__name__)
app.config.from_object(__name__)

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
@app.route("/")
def index():
    # Authentication
    if 'ticket' in request.args:
        validate(request.args['ticket'])
    title = "Rice Foodback"
    cur = g.db.execute('select name from serveries order by id')
    entries = [dict(title=row[0]) for row in cur.fetchall()]
    return  render_template('index.html', entries=entries)

@app.route("/student")
def student():
    return render_template('student.html')

@app.route("/chef")
def chef():
    return render_template('chef.html')

@app.route("/ratings/<servery>")
def ratings(servery):
    # TODO: translate urls into valid serverys and invalid serverys
    servery = servery.title()
    return render_template('ratings.html', servery=servery)

@app.route('/login')
def login():
    return redirect("{CAS_SERVER}/cas/login?service={SERVICE_URL}".format(**app.config) )

def validate(ticket):
    cas_validate = "{CAS_SERVER}/cas/validate?ticket={ticket}&service={SERVICE_URL}".format(ticket=ticket, **app.config)
    f = urllib.urlopen(cas_validate)
    response = f.readline()
    if response == "no\n":
        # TODO: Don't know if it works because of bad session
        flash('Unable to log in.')
    else:
        session['net_id'] = f.readline().strip()
    f.close()
    # TODO I should probably return something or make this functional...

@app.route('/logout')
def logout():
    session.pop('net_id', None)
    cas_logout = "{CAS_SERVER}/cas/logout?service={SERVICE_URL}".format(**app.config)
    flash('You were logged out')
    return redirect(cas_logout)

if __name__ == "__main__":
    app.run(debug=True)
