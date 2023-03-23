from clusters import Clusters
from http_client import HttpClient
from pulsar_admin.namespaces import Namespaces
from pulsar_admin.persistent_topics import PersistentTopics
from tenants import Tenants


class PulsarAdmin:
    def __init__(self, host, port):
        self.http_client = HttpClient(host, port)
        self.clusters = Clusters(self.http_client)
        self.tenants = Tenants(self.http_client)
        self.namespaces = Namespaces(self.http_client)
        self.persistent_topics = PersistentTopics(self.http_client)

