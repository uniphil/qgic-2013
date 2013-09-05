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
    app.run(debug=True)

if __name__ == '__main__':
    manager.run()
