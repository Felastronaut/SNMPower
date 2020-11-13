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

WORKDIR /home/poller