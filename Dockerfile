FROM python:3.9-alpine3.13
LABEL maintainer=" Aleksandar Petrovic aleksandar.petrovicvr@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app
COPY ./sh_scripts /sh_scripts

WORKDIR /app
EXPOSE 8000

RUN python3 -m venv /myenv && \
    /myenv/bin/pip install --upgrade pip && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add --no-cache mariadb-dev && \
    apk add linux-headers && \
    /myenv/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /static_data/static && \
    mkdir -p /static_data/media && \
    chown -R app:app /static_data && \
    chmod -R 755 /static_data && \
    chmod -R +x /sh_scripts

ENV PATH="/sh_scripts:/myenv/bin:$PATH"

USER app

CMD ["run_app.sh"]