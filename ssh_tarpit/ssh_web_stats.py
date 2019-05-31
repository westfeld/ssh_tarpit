# coding: utf-8


import datetime
import json
from twisted.logger import Logger
from twisted.web import resource


class SSHTarpitStatisticsResource(resource.Resource):
    isLeaf = True
    log = Logger()

    def __init__(self, tarpit_factory, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tarpit_factory = tarpit_factory

    def render_GET(self, request):
        """
        create array of open connections including ip address
        and connection duration in seconds
        """
        result = []
        now = datetime.datetime.now()

        request.setHeader(b'Content-Type', b'application/json')
        for con in self.tarpit_factory.open_connections:
            duration = now - con[0]
            ip_address = con[1]
            if ':' in ip_address.host:
                address_type = "IPv6"
            else:
                address_type = "IPv4"
            result.append({'duration': duration.total_seconds(),
                           'ip_address': ip_address.host,
                           'address_type': address_type})
        json_string = json.dumps(result, ensure_ascii=True)
        return json_string.encode('utf8')
