import unittest

from request_parser import parse_request


class TestRequestParser(unittest.TestCase):

    def setUp(self):
        self.request = 'POST / HTTP/1.1\r\nHost: localhost:5000\r\nUser-Agent: curl/7.47.0\r\nAccept: */*\r\nContent-Type: application/json\r\nContent-Length: 18\r\n\r\n{ "json": "info" }'

    def test_parse_returns_method(self):
        result = parse_request(self.request)
        self.assertEqual("POST",result['method'])

    def test_parse_returns_path(self):
        result = parse_request(self.request)
        self.assertEqual("/",result['path'])

    def test_parse_returns_version(self):
        result = parse_request(self.request)
        self.assertEqual("HTTP/1.1",result['version'])

    def test_parse_returns_headers(self):
        result = parse_request(self.request)
        self.assertGreater(len(result['headers']),0)

    def test_headers_split_on_colon(self):
        result = parse_request(self.request)
        expected = {
            'Host': 'localhost:5000',
            'User-Agent': 'curl/7.47.0',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Content-Length': '18'
        }
        for key, value in expected.items():
            self.assertEqual(value,result['headers'][key])

    def test_parse_includes_body(self):
        result = parse_request(self.request)
        self.assertTrue('body' in result)

    def test_parse_body_content(self):
        result = parse_request(self.request)
        expected = '{ "json": "info" }'
        self.assertEqual(expected,result['body'])        

unittest.main() 
