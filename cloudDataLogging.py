from elasticsearch import Elasticsearch
import json
import uuid
import socket
import os
import logging
import threading

ES_METRICS_TYPE = 'mef_model_metrics_type'
ES_INDEX_PREFIX = 'spr-mef-'
# ES_MODEL_NAME = os.environ['MEF_APPLICATION_NAME']
# ES_HOST = os.environ['MEF_ES_HOSTS']
# ES_PORT = os.environ['MEF_ES_PORT']

ES_MODEL_NAME = 'python-model'
ES_HOST = 'localhost'
ES_PORT = '9200'

ES_HOSTS_ARR = 'localhost:9200,127.0.0.1:9201'.split(',')

ES = Elasticsearch(ES_HOSTS_ARR, sniff_on_start=True,
                   sniff_on_connection_fail=True,
                   sniffer_timeout=60)

class CloudDataLogging(logging.Logger):
    def __init__(self, name, level = logging.NOTSET):
        self._count = 0
        self._countLock = threading.Lock()

        return super(CloudDataLogging, self).__init__(name, level)

    def info(self, msg, *args, **kwargs):
        self._countLock.acquire()
        self._count += 1
        self._countLock.release()

        self.saveLogMessageToCloudData(msg)

        return super(CloudDataLogging, self).info(msg, *args, **kwargs)

    def infoMetrics(self, msg, *args, **kwargs):
        self._countLock.acquire()
        self._count += 1
        self._countLock.release()

        self.saveMetricsToCloudData(msg)

        return super(CloudDataLogging, self).info(msg, *args, **kwargs)

    def saveMetricsToCloudData(CloudDataLogging, metrics):
        data = {}
        data['model_name'] = ES_MODEL_NAME
        data['host_name'] = socket.gethostname()
        data['metrics'] = metrics
        json_metrics = json.dumps(data)
        documentId = str(uuid.uuid4())
        print ('documentId = ' + documentId)
        # es = Elasticsearch(ES_HOSTS_ARR)
        res = ES.index(index=ES_INDEX_PREFIX + ES_MODEL_NAME, doc_type=ES_METRICS_TYPE, id=documentId, body=json_metrics)

    def saveLogMessageToCloudData(CloudDataLogging, message):
        data = {}
        data['model_name'] = ES_MODEL_NAME
        data['host_name'] = socket.gethostname()
        data['message'] = message
        json_metrics = json.dumps(data)
        documentId = str(uuid.uuid4())
        print ('documentId = ' + documentId)
        # es = Elasticsearch(ES_HOSTS_ARR)
        res = ES.index(index=ES_INDEX_PREFIX + ES_MODEL_NAME, doc_type=ES_METRICS_TYPE, id=documentId, body=json_metrics)