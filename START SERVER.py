f = open('port.kittm', 'r')
fread = f.read()
from http.server import HTTPServer, CGIHTTPRequestHandler
from tkinter import messagebox
if int(fread) >= 8888:
    messagebox.showerror('Starting Error', message='Error 001')
if int(fread) <= 8887:
    messagebox.showinfo('Server started', message="localhost:" + str(fread))
    print('Server Started')
    server_address = ("", int(fread))
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()




#messagebox.showinfo('Server started', message="localhost:" + str(fread))
#print('Server Started')
#server_address = ("", int(fread))
#httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
#httpd.serve_forever()




#f = open('port.kittm', 'r')
#fread = f.read()
#print('server started on')
#print('localhost:' + str(fread))
#from http.server import HTTPServer, CGIHTTPRequestHandler
#from tkinter import *
#from tkinter import messagebox
#server_address = ("", int(fread))
#httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
#httpd.serve_forever()

