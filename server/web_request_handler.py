import socketserver
import json
from request_parser import parse_request
from response_builder import *

class WebRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        buffer = ""
        while "\r\n" not in buffer:
            buffer += str(self.request.recv(4096),'ascii')

        print(buffer)
        
        body = { 
            "status": "OK",
            "working": "ofc",
            "integer": 1
        }
        response_body = json.dumps(body)
        headers = {'Content-Type': 'application/json'}
        cookie = create_cookie('request_made','true')

        response  = build_info(200,response_body)
        response += build_headers(headers)
        response += build_cookies([cookie])
        response += build_body(response_body)
        self.request.send(response.encode('ascii'))