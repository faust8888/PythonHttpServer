from elasticsearch import Elasticsearch
import json
import uuid
import socket
import os

ES_METRICS_TYPE = 'mef_model_metrics_type'
ES_INDEX_PREFIX = 'spr-mef-'
ES_MODEL_NAME = os.environ['MEF_APPLICATION_NAME']
ES_HOST = os.environ['MEF_ES_HOSTS']
ES_PORT = os.environ['MEF_ES_PORT']


def logMetrics(metrics):
    print (ES_MODEL_NAME)
    print (ES_HOST)
    print (ES_PORT)
    data = {}
    data['model_name'] = ES_MODEL_NAME
    data['host_name'] = socket.gethostname()
    data['metrics'] = metrics
    json_metrics = json.dumps(data)
    documentId = str(uuid.uuid4())
    print ('documentId = ' + documentId)
    es = Elasticsearch([{'host': ES_HOST, 'port': ES_PORT}])
    res = es.index(index=ES_INDEX_PREFIX + ES_MODEL_NAME, doc_type=ES_METRICS_TYPE, id=documentId, body=json_metrics)