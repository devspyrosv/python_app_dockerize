FROM python:3.7-alpine
MAINTAINER Spyros Vlachos <--->

# os setup
RUN apk update && apk add \
    python3-dev
RUN mkdir -p /usr/src/app_home

# install requirements using layer caching - if the requirements don't change, don't install them
COPY app/requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# move codebase over - if changed
COPY app /usr/src/app_home

WORKDIR /usr/src/app_home

# environment variables
ENV VAR3="Env var 3"

# run
CMD ["python", "-u", "main.py"]