import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from pulsar_admin.http_client import HttpClient


class MockServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        parsed_params = parse_qs(parsed_url.query)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        transformed_params = {k: v[0] for k, v in parsed_params.items()}

        response_body = f"Received GET request with path: {parsed_url.path} and params: {transformed_params}"
        self.wfile.write(response_body.encode('utf-8'))

    def do_DELETE(self):
        self.send_response(204)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response_body = f"Received POST request with data: {post_data}"
        self.wfile.write(response_body.encode('utf-8'))

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        response_body = f"Received PUT request with data: {post_data}"
        self.wfile.write(response_body.encode('utf-8'))


class TestHttpClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # start mock server in a new thread
        cls.server = HTTPServer(('localhost', 8888), MockServerRequestHandler)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        # stop mock server and wait for thread to finish
        cls.server.shutdown()
        cls.server_thread.join()

    def test_get(self):
        # create http client with mock server's address
        server_address = self.server.server_address
        http_client = HttpClient(server_address[0], server_address[1])

        # make get request with path and params
        path = "/test"
        params = {"foo": "bar", "baz": "qux"}
        status_code, response = http_client.get(path, params=params)

        # assert response matches expected format
        expected_response = f"Received GET request with path: {path} and params: {params}"
        self.assertEqual(200, status_code)
        self.assertEqual(expected_response, response)

    def test_delete(self):
        # create http client with mock server's address
        server_address = self.server.server_address
        http_client = HttpClient(server_address[0], server_address[1])

        # make get request with path and params
        path = "/test"
        params = {"foo": "bar", "baz": "qux"}
        status_code, response = http_client.delete(path, params=params)

        # assert response matches expected format
        self.assertEqual(204, status_code)
        self.assertEqual("", response)

    def test_post(self):
        # create http client with mock server's address
        server_address = self.server.server_address
        http_client = HttpClient(server_address[0], server_address[1])

        # make post request with path, data and params
        path = "/test"
        data = {"name": "test", "value": "123"}
        params = {"foo": "bar", "baz": "qux"}
        status_code, response = http_client.post(path, data=json.dumps(data), params=params)

        # assert response matches expected format
        expected_response = "Received POST request with data: " + """{"name": "test", "value": "123"}"""
        self.assertEqual(200, status_code)
        self.assertEqual(expected_response, response)

    def test_post_dict(self):
        # create http client with mock server's address
        server_address = self.server.server_address
        http_client = HttpClient(server_address[0], server_address[1])

        # make post request with path, data and params
        path = "/test"
        data = {"name": "test", "value": "123"}
        params = {"foo": "bar", "baz": "qux"}
        status_code, response = http_client.post(path, data=data, params=params)

        # assert response matches expected format
        expected_response = "Received POST request with data: " + """{"name": "test", "value": "123"}"""
        self.assertEqual(200, status_code)
        self.assertEqual(expected_response, response)

    def test_put(self):
        # create http client with mock server's address
        server_address = self.server.server_address
        http_client = HttpClient(server_address[0], server_address[1])

        # make post request with path, data and params
        path = "/test"
        data = {"name": "test", "value": "123"}
        params = {"foo": "bar", "baz": "qux"}
        status_code, response = http_client.put(path, data=json.dumps(data), params=params)

        # assert response matches expected format
        expected_response = "Received PUT request with data: " + """{"name": "test", "value": "123"}"""
        self.assertEqual(200, status_code)
        self.assertEqual(expected_response, response)
