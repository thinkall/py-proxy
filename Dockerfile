FROM amd64/python:3.6-alpine3.11

RUN pip install --no-cache-dir flask flask_cors flask_apscheduler requests

WORKDIR /workplace

COPY py-proxy.py .

RUN chgrp -R 0 /workplace
RUN chmod -R g+rwX /workplace

EXPOSE 3128

ENTRYPOINT python py-proxy.py