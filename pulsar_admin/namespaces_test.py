import unittest

from p_admin import PulsarAdmin
from pulsar_admin.random_util import RandomUtil


class TestNamespaces(unittest.TestCase):
    def setUp(self):
        self.admin = PulsarAdmin('localhost', 8080)

    def tearDown(self):
        pass

    def test_get_namespaces(self):
        namespaces = self.admin.namespaces.get_namespaces('public')
        self.assertTrue(len(namespaces) > 0)


if __name__ == '__main__':
    unittest.main()
