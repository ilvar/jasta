#!/usr/bin/env python
"""
Run development server
"""

from bottle import route, view, run
from redis import Redis

from bot.config import *

def get_status(jid):
    presence = Redis().hgetall('presence:%s' % jid) or {}
    m = presence.get('status') or ''
    s = presence.get('show') or ''
    return dict(r=presence and 1 or 0, m=m.decode('utf8'), s=s.decode('utf8'))

@route('/<jid>.json')
def status_json(jid):
    return get_status(jid)

@route('/<jid>.txt')
def status_text(jid):
    result = get_status(jid)
    return u'%s|%s|%s|\n' % (result['r'], result['s'], result['m'])

@route('/<jid>.html')
@view('index')
def status(jid):
    result = get_status(jid)
    result.update(jid=jid)
    return result

if __name__ == '__main__':
    if DEBUG:
        run(host="localhost", port=5000, debug=True)
    else:
        run(host="0.0.0.0", port=80, debug=False, server='fapws3')
