f = open('port.kittm', 'r')
fread = f.read()
print('server started on')
print('localhost:' + str(fread))
from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", int(fread))
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
