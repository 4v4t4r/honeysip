import logging

import sip


# Setup logging mechanism
logger = logging.getLogger('sip')
logConsole = logging.StreamHandler()
logConsole.setLevel(logging.DEBUG)
logConsole.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(logConsole)


if __name__ == '__main__':
    s = sip.SipSession(addr=('192.168.1.2', 5060), proto="udp")
    try:
        print "Looping now..."
        s.serve_forever()
    except KeyboardInterrupt:
        print("Closing socket...")