def serverWU():
    f = open('port.kittm', 'r')
    fread = f.read()
    from http.server import HTTPServer, CGIHTTPRequestHandler
    from tkinter import messagebox
    print('Server Started')
    server_address = ("", int(fread))
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()


