SECRET_KEY = '4444444' # you can never be sure it's random

DEBUG = False

JABBER_HOST = 'jabber.org'
JABBER_USER = 'some_user'
JABBER_PASS = 'password'

try:
    from bot.local_config import *
except ImportError, e:
    print e
    pass