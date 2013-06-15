#!/usr/bin/env python

import os

activate_this = os.path.join(os.path.dirname(__file__), '..', 'ENV', 'bin', 'activate_this.py')
if os.path.exists(activate_this):
    print 'Activating', activate_this
    execfile(activate_this, dict(__file__=activate_this))

os.chdir(os.path.join(os.path.dirname(__file__)))

import bottle

from bottle import route, view, run
from redis import Redis
from bot.config import *

@route('/<jid>.json')
def status_json(jid):
    presence = Redis().hgetall('presence:%s' % jid)
    presence.update(jid=jid)
    return presence

@route('/<jid>.html')
@view('index')
def status(jid):
    presence = Redis().hgetall('presence:%s' % jid)
    presence.update(jid=jid)
    return presence

application = bottle.app()