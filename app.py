import time
# import BaseHTTPServer
import os
import logging
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
# from cloudDataLogging import CloudDataLogging


# MEF_APPLICATION_NAME = os.environ['MEF_APPLICATION_NAME']
# MEF_PROJECT_NAME = os.environ['MEF_PROJECT_NAME']

root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

HOST_NAME = 'localhost'
PORT_NUMBER = 8080

# HOST_OS = MEF_APPLICATION_NAME + '.' + MEF_PROJECT_NAME + '.apps.test-ose.ca.sbrf.ru'


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        # if os.environ.get('OPENSHIFT_MEF_LOG_PATH') is not None:
        #     logging.basicConfig(level=logging.INFO)
        #     logging.info("NOOO", time.asctime())
        # else:

        # logging.setLoggerClass(CloudDataLogging)

        # logger = logging.getLogger('CloudDataLogging')

        logging.info("GET INFO REQUEST time")

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print (time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print (time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))