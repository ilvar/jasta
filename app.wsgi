#!/usr/bin/env python

import os, sys

activate_this = os.path.join(os.path.dirname(__file__), '..', 'ENV', 'bin', 'activate_this.py')
if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))

cur_path = os.path.join(os.path.dirname(__file__))
os.chdir(cur_path)
sys.path.insert(0, cur_path)

import bottle
from runserver import *
application = bottle.app()