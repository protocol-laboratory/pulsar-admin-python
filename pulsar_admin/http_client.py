import json
from urllib import parse
from urllib import request


class HttpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get(self, path, params=None):
        url = self._build_url(path, params)
        req = request.Request(url)
        with request.urlopen(req) as response:
            status_code = response.status
            return status_code, response.read().decode('utf-8')

    def delete(self, path, params=None):
        url = self._build_url(path, params)
        headers = {'Content-Type': 'application/json'}
        req = request.Request(url, headers=headers, method='DELETE')
        with request.urlopen(req) as response:
            status_code = response.status
            return status_code, response.read().decode('utf-8')

    def post(self, path, data=None, params=None):
        url = self._build_url(path, params)
        data = self._encode_data(data)
        headers = {'Content-Type': 'application/json'}
        req = request.Request(url, data, headers=headers)
        with request.urlopen(req) as response:
            status_code = response.status
            return status_code, response.read().decode('utf-8')

    def put(self, path, data=None, params=None):
        url = self._build_url(path, params)
        data = self._encode_data(data)
        headers = {'Content-Type': 'application/json'}
        req = request.Request(url, data, headers=headers, method='PUT')
        with request.urlopen(req) as response:
            status_code = response.status
            return status_code, response.read().decode('utf-8')

    def _build_url(self, path, params=None):
        url = f'http://{self.host}:{self.port}{path}'
        if params:
            encoded_params = parse.urlencode(params)
            url += '?' + encoded_params
        return url

    def _encode_data(self, data):
        if data:
            if isinstance(data, dict):
                data = json.dumps(data).encode('utf-8')
            elif isinstance(data, str):
                data = data.encode('utf-8')
        return data
