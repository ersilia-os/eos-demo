FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install flaml==0.6.9
RUN pip install lightgbm==2.3.1

WORKDIR /repo
COPY ./repo
