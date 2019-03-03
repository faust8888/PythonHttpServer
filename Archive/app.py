import time
# import BaseHTTPServer
import os
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import cloudDataLogging


MEF_APPLICATION_NAME = os.environ['MEF_APPLICATION_NAME']
MEF_PROJECT_NAME = os.environ['MEF_PROJECT_NAME']

HOST_NAME = 'localhost'
PORT_NUMBER = 8080

HOST_OS = MEF_APPLICATION_NAME + '.' + MEF_PROJECT_NAME + '.apps.test-ose.ca.sbrf.ru'


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        # print(res['result'])
        # res = es.get(index="dictionary", doc_type='dictionary_type', id=1)
        # print(res['_source'])
        cloudDataLogging.logMetrics("test")
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        #
        # print (time.asctime(), "FileBeat: Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
        # print (os.environ)
        # if os.environ.get('OPENSHIFT_MEF_LOG_PATH') is not None:
        #     logging.basicConfig(level=logging.INFO)
        #     logging.info("NOOO", time.asctime())
        # else:
        # logging.basicConfig(filename=os.environ['OPENSHIFT_MEF_LOG_PATH'] + '/model.log', filemode='a', level=logging.INFO)

        # logging.debug("GET DEBUG REQUEST time - %s", time.asctime())
        # logging.info("GET INFO REQUEST time - %s", time.asctime())
        # logging.warning("GET WARNING REQUEST time - %s", time.asctime())

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