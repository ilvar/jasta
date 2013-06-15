#!/usr/bin/env python

import os

activate_this = os.path.join(os.path.dirname(__file__), '..', 'ENV', 'bin', 'activate_this.py')
if os.path.exists(activate_this):
    print 'Activating', activate_this
    execfile(activate_this, dict(__file__=activate_this))

os.chdir(os.path.join(os.path.dirname(__file__)))

from runserver import *
import bottle

application = bottle.default_app()