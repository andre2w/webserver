import socket
from request_parser import parse_request
from response_builder import *

#Starts a server socket listening the the port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1',5000))
sock.listen(5)

print("Starting webserver in the port 5000")
print("\tURL: 127.0.0.1:5000")
print("Press Ctrl - C to stop the server")
(clientsocket, address) = sock.accept()

buffer = ""
while "\r\n" not in buffer:
    buffer += str(clientsocket.recv(4096),'ascii')

print(parse_request(buffer))
body = '{ "return": "info" }'
headers = {'Content-Type': 'application/json'}
cookie = create_cookie('request_made','true')

response  = build_info(200,body)
response += build_headers(headers)
response += build_cookies([cookie])
response += build_body(body)

clientsocket.send(response.encode('ascii'))
clientsocket.close()
