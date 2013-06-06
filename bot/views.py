#!/usr/bin/env python
"""
Main views
"""

from flask import render_template
from redis import Redis

from bot import app

@app.route('/<jid>/')
def index(jid):
    status = Redis().get('status:%s' % jid)
    show = Redis().get('show:%s' % jid)
    return render_template('index.html', status=status, show=show, jid=jid)
