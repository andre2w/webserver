import unittest
from response_builder import build_response

class TestResponseBuilder(unittest.TestCase):
    """Tests for build_response function"""
    
    def setUp(self):
        self.content = '{ "return": "info" }'

    def test_response_contains_status_code(self):
        response = build_response(200,self.content)
        self.assertTrue(response.startswith('HTTP/1.1 200 OK'))

    def test_response_contains_content_length(self):
        response = build_response(200,self.content)
        response = response.split('\r\n')[1]
        expected = f"Content-Length: {str(len(self.content))}"
        self.assertEqual(expected,response)
        
    def test_response_contains_content(self):
        response = build_response(200,self.content)
        self.assertTrue(self.content in response)

    def test_response_has_separator_from_head_and_body(self):
        response = build_response(200,self.content)
        self.assertTrue('\r\n\r\n' in response)

    def test_response_should_contain_headers(self):
        headers = {'Content-Type': 'application/json'}
        response = build_response(200,self.content,headers)
        self.assertTrue('Content-Type: application/json' in response)
        
unittest.main()