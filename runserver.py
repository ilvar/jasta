#!/usr/bin/env python
"""
Run development server
"""

from bottle import route, view, run
from redis import Redis
from bot.config import *

@route('/<jid>.json')
def status_json(jid):
    status = Redis().get('status:%s' % jid)
    show = Redis().get('show:%s' % jid)
    return dict(status=status, show=show, jid=jid)

@route('/<jid>.html')
@view('index')
def status(jid):
    status = Redis().get('status:%s' % jid)
    show = Redis().get('show:%s' % jid)
    return dict(status=status, show=show, jid=jid)

if __name__ == '__main__':
    run(host='localhost', port=5000, debug=DEBUG)
