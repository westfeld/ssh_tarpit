# coding: utf-8

import datetime
import secrets
import sys
from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from twisted.logger import Logger, globalLogPublisher, textFileLogObserver


class SSHTarpitProtocol(Protocol):
    log = Logger()

    def __init__(self):
        # LooingCall for sending random bytes
        self.lc = None
        self.send_interval = 10
        self.connection_timestamp = None
        super().__init__()

    def sendRandomBytes(self):
        """
        Method which sends a number of random bytes over the established
        TCP connection
        """
        self.transport.write(bytes(secrets.token_bytes(128)))

    def connectionMade(self):
        """
        Method in which the timestamp when the connection was made is
        recorded. Combined with the IP address of the remote peer it
        is saved in a set in the factory.
        """
        self.connection_timestamp = datetime.datetime.now()
        self.factory.open_connections.add((self.connection_timestamp,
                                           self.transport.getPeer()))
        self.lc = LoopingCall(self.sendRandomBytes)
        self.lc.start(self.send_interval)
        self.log.info("Connection made from: {address}",
                      address=self.transport.getPeer())

    def connectionLost(self, reason):
        """
        Stop the looping call and remove this connection from the
        open_connection set of the factory
        """
        if self.lc and self.lc.running:
            self.lc.stop()
        self.factory.open_connections.remove((self.connection_timestamp,
                                             self.transport.getPeer()))
        self.log.info("Connection lost from: {address}."
                      "Clients connected {nClients}",
                      address=self.transport.getPeer(),
                      nClients=len(self.factory.open_connections))


class SSHTarpitFactory(Factory):
    """
    Basic factory which has an additional attribute to bookkeep the
    open connections
    """
    protocol = SSHTarpitProtocol

    def __init__(self):
        self.open_connections = set()


def main():
    globalLogPublisher.addObserver(textFileLogObserver(sys.stdout))
    reactor.listenTCP(2020, SSHTarpitFactory())
    reactor.run()


if __name__ == "__main__":
    main()
