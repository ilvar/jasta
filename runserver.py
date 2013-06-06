#!/usr/bin/env python
"""
Run development server
"""

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

if __name__ == '__main__':
    run(host='localhost', port=5000, debug=DEBUG)
