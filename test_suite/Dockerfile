FROM python:3

ADD 01_cluster_health.py
ADD 02_insert_data.py
ADD 03_query_index.py
ADD 04_delete_data.py

RUN pip3 install boto3
RUN pip3 install elasticsearch
RUN pip3 install re
RUN pip3 install json
RUN pip3 install requests
RUN pip3 install requests_aws4auth


CMD [ "sh", "run_tests.sh" ]