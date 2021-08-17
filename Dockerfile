FROM python:3.9-alpine3.13
LABEL maintainer=" Aleksandar Petrovic aleksandar.petrovicvr@gmail.com"

ENV PYTHONUNBUFFERED 1
RUN mkdir /app

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

RUN python3 -m venv /myenv && \
    /myenv/bin/pip install --upgrade pip && \

    # add dependencies for mysqlclient library
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add --no-cache mariadb-dev && \

    /myenv/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /static_data/static_data && \
    mkdir -p /static_data/media && \
    chown -R app:app /static_data && \
    chmod -R 755 /static_data



ENV PATH="/myenv/bin:$PATH"

USER app