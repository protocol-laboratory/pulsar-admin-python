import unittest

from pulsar_admin.p_admin import PulsarAdmin
from pulsar_admin.random_util import RandomUtil


class TestTenants(unittest.TestCase):
    def setUp(self):
        self.admin = PulsarAdmin('localhost', 8080)

    def tearDown(self):
        pass

    def test_create_and_delete_tenant(self):
        # Create a new tenant
        tenant_name = RandomUtil.random_string()
        self.admin.tenants.create_tenant(tenant_name, {'allowedClusters': ['standalone']})
        tenants = self.admin.tenants.get_tenants()
        self.assertIn(tenant_name, tenants)

        # Delete the tenant
        self.admin.tenants.delete_tenant(tenant_name, False)
        tenants = self.admin.tenants.get_tenants()
        self.assertNotIn(tenant_name, tenants)


if __name__ == '__main__':
    unittest.main()
