import logging

import gevent

import sip


# Setup logging mechanism
logger = logging.getLogger('sip')
logConsole = logging.StreamHandler()
logConsole.setLevel(logging.DEBUG)
logConsole.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(logConsole)


class SIPServer(DatagramServer):

    def handle(self, data, address):
        print '%s: got %r' % (address[0], data)
        self.socket.sendto('Received %s bytes' % len(data), address)


if __name__ == '__main__':
    s = sip.SipSession(proto="udp")
    s.bind(('localhost', 5060))

    try:
        print "Looping now..."
        SIPServer('localhost:5060').serve_forever()
    except KeyboardInterrupt:
        print("Closing socket...")