import time
import BaseHTTPServer
import os
import logging


HOST_NAME = 'localhost'
PORT_NUMBER = 8007


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
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
        s.wfile.write("<p>HOME: %s</p>" % os.environ['HOME'])
        s.wfile.write("</body></html>")
        print (time.asctime(), "FileBeat: Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
        logging.basicConfig(level=logging.INFO)
        logging.debug("GET DEBUG REQUEST time - %s", time.asctime())
        logging.info("GET INFO REQUEST time - %s", time.asctime())
        logging.warning("GET WARNING REQUEST time - %s", time.asctime())

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print (time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print (time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))