FROM registry.access.redhat.com/openshift3/logging-fluentd

RUN useradd fluentd -g root

COPY fluentdHelps fluentdHelps

RUN mkdir /var/log/fluentd && \
    cp fluentdHelps/mef-fluentd.conf /var/log/mef-fluentd.conf && \
    chmod -R 775 /var/log/fluentd && \
    chown -R fluentd:root /var/log/fluentd

ADD fluentdHelps/mef-fluentd.conf  /var/log/
ADD fluentdHelps/run.sh /var/log/

#CMD ["fluentd", "-vv", "-c", "/var/log/mef-fluentd.conf"]
CMD ["sh", "/var/log/run.sh"]