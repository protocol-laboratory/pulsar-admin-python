import json

from pulsar_admin.http_client import HttpClient
from pulsar_admin.pulsar_admin_exception import PulsarAdminException
from pulsar_admin.tenant_info import TenantInfo
from pulsar_admin.url_const import UrlConst


class Tenants:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def create_tenant(self, tenant, tenant_info: TenantInfo):
        endpoint = f"{UrlConst.TENANTS}/{tenant}"
        data = json.dumps(tenant_info)
        status_code, response = self.http_client.put(endpoint, data=data)
        if status_code != 204:
            raise PulsarAdminException(
                f"failed to create tenant {tenant}, status code {status_code}, response: {response}")

    def delete_tenant(self, tenant, force):
        endpoint = f"{UrlConst.TENANTS}/{tenant}"
        params = {"force": force}
        status_code, response = self.http_client.delete(endpoint, params=params)
        if status_code != 204:
            raise PulsarAdminException(
                f"failed to delete tenant {tenant}, status code {status_code}, response: {response}")

    def update_tenant(self, tenant, tenant_info):
        endpoint = f"{UrlConst.TENANTS}/{tenant}"
        data = json.dumps(tenant_info)
        status_code, response = self.http_client.post(endpoint, data=data)
        if status_code != 204:
            raise PulsarAdminException(
                f"failed to update tenant {tenant}, status code {status_code}, response: {response}")

    def get_tenants(self):
        endpoint = UrlConst.TENANTS
        status_code, response = self.http_client.get(endpoint)
        if status_code != 200:
            raise PulsarAdminException(f"failed to get tenants, status code {status_code}, response: {response}")
        return json.loads(response)
