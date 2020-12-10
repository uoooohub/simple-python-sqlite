FROM python:3.8-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
VOLUME /root/10/src:/code
RUN mkdir data
RUN echo $(ls)
ADD main.py /code/
RUN python main.py
ADD . /code/