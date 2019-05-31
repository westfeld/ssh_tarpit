# coding: utf-8

from zope.interface import implementer

from twisted.python import usage
from twisted.plugin import IPlugin
from twisted.application.service import IServiceMaker, MultiService
from twisted.application import internet
from twisted.web import server

from ssh_tarpit.ssh_tarpit import SSHTarpitFactory
from ssh_tarpit.ssh_web_stats import SSHTarpitStatisticsResource


class Options(usage.Options):
    optParameters = [["port", "p", 22, "The port number to listen on."],
                     ["bind", "b", "0.0.0.0", "The bind address the server is "
                      "responding to, empty means all addresses"],
                     ["http_port", "t", "8080", "The port number the HTTP server is "
                      "listening on"],
                     ["http_bind", "s", "localhost", "The bind address the "
                      "HTTP server is listening."]
                     ]


@implementer(IServiceMaker, IPlugin)
class SSHTarpitServiceMaker(object):
    tapname = "SSHTarpit"
    description = "Server keeps SSH connections open indefinetely"
    options = Options

    def makeService(self, options):
        """
        Construct a TCPServer from a factory defined in ssh_tarpit
        """
        multi_service = MultiService()
        ssh_tarpit_factory = SSHTarpitFactory()
        internet.TCPServer(int(options["port"]), ssh_tarpit_factory,
                           interface=options["bind"]).setServiceParent(multi_service)
        site = server.Site(SSHTarpitStatisticsResource(ssh_tarpit_factory))
        internet.TCPServer(int(options["http_port"]), site,
                           interface=options['http_bind']).setServiceParent(multi_service)
        return multi_service


# Now construct an object which *provides* the relevant interfaces
# The name of this variable is irrelevant, as long as there is *some*
# name bound to a provider of IPlugin and IServiceMaker.

serviceMaker = SSHTarpitServiceMaker()
