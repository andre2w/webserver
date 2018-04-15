import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../server')))
from request_parser import parse_request


class TestRequestParser(unittest.TestCase):

    def setUp(self):
        self.request =  'POST / HTTP/1.1\r\n'
        self.request += 'Host: localhost:5000\r\n'
        self.request += 'User-Agent: curl/7.47.0\r\n'
        self.request += 'Accept: */*\r\n'
        self.request += 'Content-Type: application/json\r\n'
        self.request += 'Content-Length: 18\r\n'
        self.request += 'Cookie: cookie1=value, httponly=false; cookie2=othervalue\r\n'
        self.request += '\r\n'
        self.request += '{ "json": "info" }'

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

    def test_parse_returns_cookies(self):
        result = parse_request(self.request)
        self.assertTrue('cookies' in result)

    def test_parse_returns_cookies_content(self):
        result = parse_request(self.request)
        self.assertEqual('value',result['cookies']['cookie1']['value'])
        self.assertEqual('false',result['cookies']['cookie1']['httponly'])
        self.assertEqual('othervalue',result['cookies']['cookie2']['value'])

unittest.main() 
