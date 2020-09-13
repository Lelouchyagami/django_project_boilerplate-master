FROM python:3.5
MAINTAINER Parth

RUN mkdir /django_project_boilerplate-master
WORKDIR /django_project_boilerplate-master
ADD . /django_project_boilerplate-master/

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

ENV PORT=8000

RUN apt-get update && apt-get install -y --no-install-recommends \
	tzdata \
	python3-setuptools \
	python3-pip \
	python3-dev \
	python3-venv \
	git \
	&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pip install -r requirements.txt

EXPOSE 8888
CMD gunicorn djecommerce.wsgi:application --bind 0.0.0.0:8000:$PORT
