import json
from typing import Dict

from pulsar_admin.http_client import HttpClient

from pulsar_admin.pulsar_admin_exception import PulsarAdminException
from pulsar_admin.url_const import UrlConst


class PersistentTopics:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def create_partitioned_topic(self, tenant: str, namespace: str, topic: str, num_partitions: int,
                                 create_local_topic_only: bool = False):
        params = [("createLocalTopicOnly", str(create_local_topic_only))]
        status_code, _ = self.http_client.put(
            f"{UrlConst.PERSISTENT}/{tenant}/{namespace}/{topic}{UrlConst.PARTITIONS}",
            json.dumps(num_partitions),
            params=params
        )
        if status_code != 204:
            raise PulsarAdminException(f"failed to create partitioned topic {tenant}/{namespace}/{topic}, "
                                       f"status code {status_code}")

    def delete_partitioned_topic(self, tenant: str, namespace: str, topic: str, force: bool = False,
                                 authoritative: bool = False):
        params = [("force", str(force)), ("authoritative", str(authoritative))]
        status_code, _ = self.http_client.delete(
            f"{UrlConst.PERSISTENT}/{tenant}/{namespace}/{topic}{UrlConst.PARTITIONS}",
            params=params
        )
        if status_code != 204:
            raise PulsarAdminException(f"failed to delete partitioned topic {tenant}/{namespace}/{topic}, "
                                       f"status code {status_code}")

    def create_topic(self, tenant: str, namespace: str, topic: str, authoritative: bool = False,
                     properties: Dict[str, str] = None):
        params = [("authoritative", str(authoritative))]
        status_code, _ = self.http_client.put(
            f"{UrlConst.PERSISTENT}/{tenant}/{namespace}/{topic}",
            json.dumps(properties) if properties else None,
            params=params
        )
        if status_code != 204:
            raise PulsarAdminException(f"failed to create non-partitioned topic {tenant}/{namespace}/{topic}, "
                                       f"status code {status_code}")

    def delete_topic(self, tenant: str, namespace: str, topic: str, force: bool = False, authoritative: bool = False):
        params = [("force", str(force)), ("authoritative", str(authoritative))]
        status_code, _ = self.http_client.delete(
            f"{UrlConst.PERSISTENT}/{tenant}/{namespace}/{topic}",
            params=params
        )
        if status_code != 204:
            raise PulsarAdminException(f"failed to delete non-partitioned topic {tenant}/{namespace}/{topic}, "
                                       f"status code {status_code}")

    def get_partitioned_topic_list(self, tenant: str, namespace: str, include_system_topic: bool = False):
        params = [("includeSystemTopic", include_system_topic)]
        url = f"{UrlConst.PERSISTENT}/{tenant}/{namespace}{UrlConst.PARTITIONED}"
        status_code, subscriptions = self.http_client.get(url, params=params)
        if status_code != 200:
            raise PulsarAdminException(f"failed to get partitioned topic for namespace {tenant}/{namespace}, "
                                       f"status code {status_code}")
        return json.loads(subscriptions)

    def get_subscription(self, tenant: str, namespace: str, topic: str, authoritative: bool = False) -> list:
        params = [("authoritative", authoritative)]
        url = f"{UrlConst.PERSISTENT}/{tenant}/{namespace}/{topic}/subscriptions"
        status_code, subscriptions = self.http_client.get(url, params=params)
        if status_code != 200:
            raise PulsarAdminException(f"failed to get subscriptions for topic {tenant}/{namespace}/{topic}, "
                                       f"status code {status_code}")
        return json.loads(subscriptions)
