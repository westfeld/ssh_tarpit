# coding: utf-8

from zope.interface import implementer

from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker
from twisted.application import internet

from ssh_tarpit.ssh_tarpit import SSHTarpitFactory


class Options(usage.Options):
    optParameters = [["port", "p", 22, "The port number to listen on."],
                     ["bind", "b", "0.0.0.0", "The bind address the server is "
                      "responding to, empty means all addresses"]
                     ]


@implementer(IServiceMaker, IPlugin)
class SSHTarpitServiceMaker(object):
    tapname = "SSHTarpit"
    description = "Server keeps SSH connections open indefinetely"
    options = Options

    def makeService(self, options):
        """
        Construct a TCPServer from a factory defined in myproject.
        """
        return internet.TCPServer(int(options["port"]), SSHTarpitFactory(),
                                  interface=options["bind"])


# Now construct an object which *provides* the relevant interfaces
# The name of this variable is irrelevant, as long as there is *some*
# name bound to a provider of IPlugin and IServiceMaker.

serviceMaker = SSHTarpitServiceMaker()
