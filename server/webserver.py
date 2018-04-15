import socketserver
from web_request_handler import WebRequestHandler

if __name__ == '__main__':
    try:
        address = ('localhost',5000)
        server = socketserver.TCPServer(address,WebRequestHandler)
        server.serve_forever()
    except (KeyboardInterrupt):
        server.shutdown()
        server.server_close()