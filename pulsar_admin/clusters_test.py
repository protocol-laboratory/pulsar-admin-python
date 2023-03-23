import unittest

from pulsar_admin.clusters import Clusters
from pulsar_admin.http_client import HttpClient


class TestClusters(unittest.TestCase):
    def setUp(self):
        self.http_client = HttpClient('localhost', 8080)

    def tearDown(self):
        pass

    def test_get_clusters(self):
        # create clusters object using http client
        clusters = Clusters(self.http_client)

        # call getClusters method and verify response
        cluster_list = clusters.get_clusters()
        self.assertIsInstance(cluster_list, list)
