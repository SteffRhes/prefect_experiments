FROM basex/basexhttp:9.5.2
USER root
RUN apk update
RUN apk add shadow
RUN usermod -u 1000 basex
RUN groupmod -g 1000 basex
RUN mkdir -p /veld/storage
RUN chown -R basex:basex /veld
USER basex
COPY ./basex_config /srv/basex/.basex
EXPOSE 8984

