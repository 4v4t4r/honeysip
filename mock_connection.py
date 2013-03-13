################################################################################
#
# Stand-alone VoIP honeypot client (preparation for Dionaea integration)
# Copyright (c) 2010 Tobias Wulff (twu200 at gmail)
#
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# 
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
# Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
################################################################################

import socket
import asyncore
import logging
import sys
import traceback

logger = logging.getLogger('sip')
logger.setLevel(logging.DEBUG)


class connection(asyncore.dispatcher):
    """Connection class mockup (from connection.pyx in dionaea src)"""

    def __init__(self, proto=None, sock=None):
        """Creates a new connection with TCP as its default transport
        protocol"""
        asyncore.dispatcher.__init__(self, sock)

        if not sock:
            # Use TCP by default, and UDP if stated
            socket_type = socket.SOCK_STREAM
            if proto and proto.lower() == 'udp':
                socket_type = socket.SOCK_DGRAM

            # Create non-blocking socket
            self.create_socket(socket.AF_INET, socket_type)

    def handle_established(self):
        """Callback for a newly established connection (client or server)"""
        logger.info('Session established')
        logger.debug('Session socket: {}'.format(self.getsockname()))

    def handle_read(self):
        """Callback for incoming data (dionaea: handle_io_in)"""
        logger.info('handle read')
        print self.recv(8192)

    def writable(self):
        logger.info('writable')
        pass

    def handle_write(self):
        logger.info('handle write')

    def handle_connect(self):
        """Callback for successful connect (client)"""
        logger.info('handle established')
        self.handle_established()

    def handle_close(self):
        """Callback for a closed connection"""
        logger.info('Session closed')
        self.close()

    def handle_accept(self):
        """Callback for successful accept (server)"""
        logger.info('handle accept')
        self.__conn, self.__address = self.accept()
        self.handle_established()

    def handle_error(self):
        logger.error('handle error')
        traceback.print_exc(file=sys.stdout)

    def send(self, data, address):
        logger.info('handle send')
        result = self.socket.sendto(data, address)
        print result