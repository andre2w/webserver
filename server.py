import socket
from request_parser import parse_request
from response_builder import build_response

#Starts a server socket listening the the port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1',5000))
sock.listen(5)

(clientsocket, address) = sock.accept()

buffer = ""
while "\r\n" not in buffer:
    buffer += str(clientsocket.recv(4096),'ascii')

body = '{ "return": "info" }'
headers = {'Content-Type': 'application/json'}
response = build_response(200,body,headers)
clientsocket.send(response.encode('ascii'))

clientsocket.close()
