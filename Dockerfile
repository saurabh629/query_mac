FROM python:alpine3.7
WORKDIR /query_mac/
ADD . /query_mac/
RUN pip install -r requirements.txt
CMD python query_mac.py
