#!/usr/bin/env python3

import logging

from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout


class JabberBot(ClientXMPP):

    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

    def session_start(self, event):
        self.send_presence()
        self.contacts = self.get_roster()['roster']['items'].keys()

    def message(self, msg):
        if msg['type'] in ('chat', 'normal'):
            for contact in self.contacts:
                mfrom = str(msg['from']).split('@')[0]
                mto = str(contact)

                if mfrom in mto:
                    # Do net send message to himself.
                    continue

                body = (
                    'User {}:\n{}'.format(mfrom, msg['body'])
                )
                self.send_message(mto=contact, mbody=body)


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING,
                        format='%(levelname)-8s %(message)s')

    xmpp = JabberBot('bot_name@hostname', 'password')
    xmpp.connect()
    xmpp.process(block=True)
