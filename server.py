import socket
from request_parser import parse_request

#Starts a server socket listening the the port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1',5000))
sock.listen(5)

(clientsocket, address) = sock.accept()

buffer = ""
while "\r\n" not in buffer:
    buffer += str(clientsocket.recv(4096),'ascii')

print(parse_request(buffer))

clientsocket.send('HTTP/1.1 200 OK \r\n'.encode('ascii'))
clientsocket.send('\r\n'.encode('ascii'))
clientsocket.send('YEAH'.encode('ascii'))

clientsocket.close()
sock.close()

