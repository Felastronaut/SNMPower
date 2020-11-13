FROM alpine:latest

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN apk add build-base
RUN apk add net-snmp
RUN apk add net-snmp-libs
RUN apk add jq
RUN apk add snmp

RUN addgroup -g 1000 -S poller && \
    adduser -u 1000 -S poller -G poller
USER poller

RUN apk add docker
RUN docker run -d \
-p 3000:3000 \
--name=grafana \
-e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource" \
grafana/grafana

WORKDIR /home/poller