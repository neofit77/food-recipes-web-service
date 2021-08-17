FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="Aleksandar Petrovic aleksandar.petrovicvr@gmail.com"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=9000

USER root

RUN mkdir -p /web/static && \
    chmod 755 /web/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /web/static

USER nginx

CMD ["/run.sh"]