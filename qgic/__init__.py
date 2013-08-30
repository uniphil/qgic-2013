# -*- coding: utf-8 -*-
"""
    qgic
    ~~~~

    Website for the Queen's Global Innovation Conference (2013)

    blah blah blah
"""

from flask import Flask, render_template
from flask.ext.assets import Environment

app = Flask(__name__)
assets = Environment(app)


@app.route('/')
def home():
    return render_template('home.html')
