FROM alpine:latest

RUN addgroup -g 1000 -S poller && \
    adduser -u 1000 -S poller -G poller
USER poller

WORKDIR /home/poller