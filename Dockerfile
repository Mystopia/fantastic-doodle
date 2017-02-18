FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
ADD . /src/
RUN pip install -r requirements.txt
