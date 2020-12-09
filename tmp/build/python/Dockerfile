FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /var/www/html
WORKDIR /var/www/html
ADD requirements.txt /var/www/html/
RUN pip install -r requirements.txt
ADD . /var/www/html/