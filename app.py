import time
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


HOST_NAME = 'http://test-server-myproject.192.168.99.101.nip.io'
PORT_NUMBER = 8080


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body><p>This is a test.</p>")
        s.wfile.write("<time.asctime()>HOME: %s</p>" % os.environ['HOME'])
        s.wfile.write("<p>ILYA_MERKUREV_VAR: %s</p>" % os.environ['ILYA_MERKUREV_VAR'])
        s.wfile.write("</body></html>")

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print (time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
