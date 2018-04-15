import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../server')))

from response_builder import build_info, build_headers, create_cookie, build_cookies, build_body

class TestResponseBuilder(unittest.TestCase):
    """Tests for response_builder functions"""
    
    def setUp(self):
        self.content = '{ "return": "info" }'

    def test_build_info(self):
        response = build_info(200,self.content)
        expect   = f"HTTP/1.1 200 OK\r\nContent-Length: {str(len(self.content))}\r\n"
        self.assertEqual(expect,response)

    def test_response_contains_content_length(self):
        headers_to_build = {
            "Content-Type": "application/json",
            "Accept-Language": "en-US;en"
        }       
        response = build_headers(headers_to_build)
        expected = "Content-Type: application/json\r\nAccept-Language: en-US;en\r\n"
        self.assertEqual(expected,response)
        
    def test_cookie_creator(self):
        cookie = create_cookie("test","cookie-value")
        self.assertEqual('cookie-value',cookie['value'])
        self.assertEqual(False,cookie['secure'])
        self.assertEqual(False,cookie['httponly'])

    def test_build_cookie(self):
        cookie = create_cookie("test","cookie-value")
        response = build_cookies([cookie])
        expected = "Set-Cookie: test=cookie-value\r\n"
        self.assertEqual(response,expected)

    def test_build_cookie_with_extra_args(self):
        cookie = create_cookie("test","cookie-value",None,True,True)
        response = build_cookies([cookie])
        expected = "Set-Cookie: test=cookie-value; Secure; HttpOnly\r\n"
        self.assertEqual(response,expected)

    def test_build_response_body(self):
        expected = f"\r\n{self.content}\r\n"
        body = build_body(self.content)
        self.assertEqual(expected,body)

    def test_build_entire_response(self):
        expected = (
            'HTTP/1.1 200 OK\r\n'
            'Content-Length: 20\r\n'
            'Content-Type: application/json\r\n'
            'Accept-Language: en-US;en\r\n'
            'Set-Cookie: test=cookie-value; Secure; HttpOnly\r\n'
            '\r\n'
            '{ "return": "info" }\r\n'
        )
        response = build_info(200,self.content)

        headers_to_build = {
            "Content-Type": "application/json",
            "Accept-Language": "en-US;en"
        }       
        response += build_headers(headers_to_build)
        cookie    = create_cookie("test","cookie-value",None,True,True)
        response += build_cookies([cookie])
        response += build_body(self.content)
        self.assertEqual(expected,response)

unittest.main()