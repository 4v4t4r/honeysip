import logging

# Setup logging mechanism
logger = logging.getLogger('sip')
logConsole = logging.StreamHandler()
logConsole.setLevel(logging.DEBUG)
logConsole.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger.addHandler(logConsole)

import sip


if __name__ == '__main__':
    sip_session = sip.SipSession(addr=('localhost', 5060), proto="udp")
    try:
        sip_session.serve_forever()
    except KeyboardInterrupt:
        print("Closing socket...")