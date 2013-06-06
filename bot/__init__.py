"""
Main app module
"""

import sys

from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('config.py')
app.debug = app.config.get('DEBUG')

import bot.views
