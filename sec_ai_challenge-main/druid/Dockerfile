FROM openjdk:8-jre

LABEL maintainer="SECURITY.AI challenge"

RUN set -ex \
    && apt-get update \
    && apt-get install -y --no-install-recommends python3 libfindbin-libs-perl

COPY ./apache-druid-0.20.0-bin.tar.gz /tmp/

RUN set -ex \
    && mkdir -p /opt/druid \
    && tar xz -f /tmp/apache-druid-0.20.0-bin.tar.gz --strip-components 1 -C /opt/druid

EXPOSE 8888
WORKDIR /opt/druid
CMD [ "/opt/druid/bin/start-nano-quickstart" ]