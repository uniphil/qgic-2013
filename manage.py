#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    manage
    ~~~~~~

    manage the project blah blah
"""

from flask.ext.script import Manager

from qgic import app, assets

manager = Manager(app)

@manager.command
def runserver():
    from os import environ as env
    app.run(debug=True, host='0.0.0.0', port=int(env.get('PORT', '5000')))

@manager.command
def runnodebug():
    from os import environ as env
    app.run(host='0.0.0.0', port=int(env.get('PORT', '5000')))

if __name__ == '__main__':
    manager.run()
