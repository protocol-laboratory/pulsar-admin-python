import unittest

from pulsar_admin.p_admin import PulsarAdmin
from pulsar_admin.random_util import RandomUtil
from pulsar_admin.tenant_info import TenantInfo


class TestPersistentTopics(unittest.TestCase):
    def setUp(self):
        self.admin = PulsarAdmin('localhost', 8080)

    def tearDown(self):
        pass

    def test_create_and_delete_topic(self):
        tenant = RandomUtil.random_string()
        namespace = RandomUtil.random_string()
        topic = RandomUtil.random_string()
        tenant_info = TenantInfo(admin_roles=set(), allowed_clusters={'standalone'})
        self.admin.tenants.create_tenant(tenant, tenant_info.to_json())
        self.admin.namespaces.create_namespace(tenant, namespace)
        # Create a non-partitioned topic
        self.admin.persistent_topics.create_topic(tenant, namespace, topic, False, {})

        # Delete the topic
        self.admin.persistent_topics.delete_topic(tenant, namespace, topic, False, False)
        self.admin.namespaces.delete_namespace(tenant, namespace)
        self.admin.tenants.delete_tenant(tenant, False)

    def test_create_and_delete_partitioned_topic(self):
        tenant = RandomUtil.random_string()
        namespace = RandomUtil.random_string()
        topic = RandomUtil.random_string()
        tenant_info = TenantInfo(admin_roles=set(), allowed_clusters={'standalone'})
        self.admin.tenants.create_tenant(tenant, tenant_info.to_json())
        self.admin.namespaces.create_namespace(tenant, namespace)
        # Create a partitioned topic
        num_partitions = 3
        self.admin.persistent_topics.create_partitioned_topic(tenant, namespace, topic, num_partitions, False)
        self.assertEqual([f'persistent://{tenant}/{namespace}/{topic}'],
                         self.admin.persistent_topics.get_partitioned_topic_list(tenant, namespace, topic))

        # Delete the partitioned topic
        self.admin.persistent_topics.delete_partitioned_topic(tenant, namespace, topic, False, False)
        self.assertEqual([], self.admin.persistent_topics.get_partitioned_topic_list(tenant, namespace, topic))
        self.admin.namespaces.delete_namespace(tenant, namespace)
        self.admin.tenants.delete_tenant(tenant, False)


if __name__ == "__main__":
    unittest.main()
