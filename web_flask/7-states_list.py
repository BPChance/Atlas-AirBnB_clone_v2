#!/usr/bin/python3
""" starts a Flask web app """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ display html page with list of state objects """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_db(exception):
    """ closes storage """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
