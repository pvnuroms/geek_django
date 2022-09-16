FROM python:3.9-slim-buster

# установка часового пояся Europe/Moscow
RUN /bin/cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime && echo 'Europe/Moscow' >/etc/timezone

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /python_projects
WORKDIR /python_projects
COPY ./requirements.txt /python_projects
RUN pip install --no-cache-dir -r requirements.txt
