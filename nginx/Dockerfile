FROM ubuntu:16.04
MAINTAINER chris elliott <ctelliott@gmail.com>

RUN apt-get update && \
  apt-get install --no-install-recommends -q -y --force-yes \
    nginx \
    apache2-utils && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add nginx config.
ADD config /var/config/nginx

# Add docker-entrypoint.sh
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
