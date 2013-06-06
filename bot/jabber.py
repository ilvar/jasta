# coding: utf-8

import time

from redis import Redis
from xmpp import *

from config import JABBER_HOST, JABBER_USER, JABBER_PASS, DEBUG

class Bot:
    def run(self):
        # Born a client
        self.cl = Client(JABBER_HOST, debug=DEBUG)

        if not self.cl.connect(server=(JABBER_HOST, 5223)):
            raise IOError('Can not connect to server.')

        # ...authorize client
        if not self.cl.auth(JABBER_USER, JABBER_PASS, 'status_bot'):
            raise IOError('Can not auth with server.')

        self.jid = '%s@%s' % (JABBER_USER, JABBER_HOST)

        # ...register some handlers (if you will register them before auth they will be thrown away)
        self.cl.RegisterHandler('unknown', self.presenceHandler)
        self.cl.RegisterHandler('default', self.presenceHandler)
        self.cl.RegisterHandler('presence', self.presenceHandler)
        self.cl.RegisterHandler('message', self.presenceHandler)
        self.cl.RegisterHandler('iq', self.presenceHandler)

        # ...become available
        self.cl.sendInitPresence(False)
        self.cl.send(Presence(frm=self.jid, show='online', status='Online'))

        while 1:
            try:
                # ...work some time
                self.cl.Process(1)

                # ...if connection is brocken - restore it
                if not self.cl.isConnected():
                    self.cl.reconnectAndReauth()
            except KeyboardInterrupt:
                break
            except Exception, e:
                pass

            time.sleep(5)
            self.cl.send(Presence(frm=self.jid, show='online', status='Online'))

        # ...and then disconnect.
        self.cl.disconnect()

    def presenceHandler(self, conn, presence_node):
        jid = str(presence_node.getFrom())
        short_jid = jid.split('/')[0]

        if short_jid == self.jid:
            return

        typ = presence_node.attrs.get('type')
        if typ == 'subscribe':
            print 'Subscribing to', jid
            self.cl.send(Presence(jid, 'subscribed'))
            self.cl.send(Presence(short_jid, 'subscribe'))
        elif typ is None:
            pass
        elif typ == 'unsubscribe':
            print 'UnSubscribing to', jid
            self.cl.send(Presence(jid, 'unsubscribed'))
            self.cl.send(Presence(short_jid, 'unsubscribe'))

        show = presence_node.getShow() or 'online'
        status = presence_node.getStatus() or ''

        Redis().set('show:%s' % short_jid, show)
        Redis().set('status:%s' % short_jid, status)

