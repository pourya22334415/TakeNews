FROM python:3.11.3-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# install requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

# install selenium
RUN pip install selenium