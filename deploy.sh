#!/bin/bash

docker stop sample-app \
&& (docker rm sample-app) \
|| (docker rm sample-app && sleep 1 || sleep 1)

docker run -d -p 80:${PORT} -e PORT=${PORT} --name sample-app gcr.io/lbg-mea-14/ag-lbg-python-api