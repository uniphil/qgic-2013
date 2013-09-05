# -*- coding: utf-8 -*-
"""
    qgic
    ~~~~

    Website for the Queen's Global Innovation Conference (2013)

    blah blah blah
"""

from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

assets.url = '/static'  # HACK HACK HACK

assets.register('css_screen', Bundle('sass/screen.sass',
                filters='compass', output='css/screen.%(version)s.css'))
assets.register('css_print', Bundle('sass/print.sass',
                filters='compass', output='css/print.%(version)s.css'))

assets.register('js', Bundle('coffee/main.coffee',
                filters='coffeescript', output='js/main.%(version)s.js'))


@app.route('/')
def home():
    team_members = [
        {
            'name': 'Alicia Cuzner',
            'role': 'Speaker Coordinator',
        },
        {
            'name': 'Yaseen Khaled',
            'role': 'Speaker Coordinator',
        },
        {
            'name': 'Michael Piotrowski',
            'role': 'Innovation Challenge Coordinator',
        },
        {
            'name': 'Kirsten MacMillan',
            'role': 'Workshop Coordinator',
        },
        {
            'name': 'Sarah Luke',
            'role': 'Sponsorship & Finance',
        },
        {
            'name': 'Andrea D\'Amour',
            'role': 'Sponsorship & Finance',
        },
        {
            'name': 'Vidhur Verghese',
            'role': 'Marketing & Media',
        },
        {
            'name': 'Eric Vanular',
            'role': 'Logistics Director',
        },
        {
            'name': 'Phil Schleihauf',
            'role': 'IT Director',
        },
    ]
    return render_template('home.html', team_members=team_members)
