# -*- coding: utf-8 -*-

import KISSmetrics
from urllib3 import PoolManager


class Client:

    def __init__(self, key=None, trk_host=KISSmetrics.TRACKING_HOSTNAME,
                 trk_proto=KISSmetrics.TRACKING_PROTOCOL):
        self.key = key
        self.trk_host = trk_host
        self.trk_proto = trk_proto
        self.http = PoolManager()

    def url(self, query_string):
        return '%s://%s%s' % (self.trk_proto, self.trk_host, query_string)

    def record(self, person, event, timestamp=None, properties={},
               uri=KISSmetrics.RECORD_URI):
        pass

    def set(self, person, timestamp=None, properties={},
            uri=KISSmetrics.SET_URI):
        pass

    def alias(self, person, identity, uri=KISSmetrics.ALIAS_URI):
        pass
