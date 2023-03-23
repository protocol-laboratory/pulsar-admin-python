import json

from pulsar_admin.http_client import HttpClient
from pulsar_admin.pulsar_admin_exception import PulsarAdminException
from pulsar_admin.url_const import UrlConst


class Namespaces:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def get_namespaces(self, tenant):
        status_code, response = self.http_client.get(
            f"{UrlConst.NAMESPACES}/{tenant}"
        )
        if status_code != 200:
            raise PulsarAdminException(
                f"Failed to get namespaces of tenant {tenant}, status code {status_code}, body: {response}"
            )
        return json.loads(response)
