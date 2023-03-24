import unittest

from pulsar_admin.p_admin import PulsarAdmin
from pulsar_admin.random_util import RandomUtil
from pulsar_admin.tenant_info import TenantInfo


class TestNamespaces(unittest.TestCase):
    def setUp(self):
        self.admin = PulsarAdmin('localhost', 8080)

    def tearDown(self):
        pass

    def test_get_namespaces(self):
        namespaces = self.admin.namespaces.get_namespaces('public')
        self.assertTrue(len(namespaces) > 0)

    def test_create_and_delete_namespaces(self):
        tenant = RandomUtil.random_string()
        namespace = RandomUtil.random_string()
        tenant_info = TenantInfo(admin_roles=set(), allowed_clusters={'standalone'})
        self.admin.tenants.create_tenant(tenant, tenant_info.to_json())
        self.admin.namespaces.create_namespace(tenant, namespace)
        namespaces = self.admin.namespaces.get_namespaces(tenant)
        self.assertTrue(tenant + "/" + namespace in namespaces)
        policy = self.admin.namespaces.get_namespace_policy(tenant, namespace)
        self.admin.namespaces.delete_namespace(tenant, namespace)
        self.admin.namespaces.create_namespace(tenant, namespace, policy)
        self.admin.namespaces.delete_namespace(tenant, namespace)
        namespaces = self.admin.namespaces.get_namespaces(tenant)
        self.assertFalse(namespace in namespaces)
        self.admin.tenants.delete_tenant(tenant, False)


if __name__ == '__main__':
    unittest.main()
