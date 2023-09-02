FROM python:3.11.3-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app


# install selenium requirements
RUN apk update
RUN apk add chromium chromium-chromedriver

# install curl
RUN apk add curl

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# install requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt

# install selenium
RUN pip install selenium