FROM openjdk:8-jre

LABEL maintainer="SECURITY.AI challenge"

COPY logging.yml ./config/logging.yml
COPY docker-entrypoint.sh /

RUN set -ex \
    && mkdir -p /usr/share/elasticsearch \
    && wget -qO- https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.1.1.tar.gz | tar zx \
        --strip-components 1 -C /usr/share/elasticsearch \
    && chmod +x /docker-entrypoint.sh


ENV PATH /usr/share/elasticsearch/bin:$PATH
WORKDIR /usr/share/elasticsearch
EXPOSE 9200 9300

RUN set -ex \
    && plugin -install mobz/elasticsearch-head

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]