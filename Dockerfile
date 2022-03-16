FROM python:3.8
WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=Europe/London

RUN pip install --upgrade pip && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY ./requirements.txt /home/app/requirements.txt
RUN pip install -r requirements.txt && apt-get update && apt-get install netcat supervisor -y && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

COPY . /home/app
COPY ./config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
