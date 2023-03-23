import json
from typing import List

from pulsar_admin.http_client import HttpClient
from pulsar_admin.pulsar_admin_exception import PulsarAdminException
from pulsar_admin.url_const import UrlConst


class Clusters:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def get_clusters(self) -> List[str]:
        try:
            status_code, response = self.http_client.get(UrlConst.CLUSTERS)
            if status_code != 200:
                raise PulsarAdminException(
                    f"failed to get list of clusters, status code {response.status_code}, body: {response.text}")
            return json.loads(response)
        except Exception as e:
            raise PulsarAdminException(e)
