print('server started')
print('localhost:7777')
from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 7777)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
