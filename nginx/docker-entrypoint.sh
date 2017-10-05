#!/bin/bash
set -e

AUTH_USER=${AUTH_USER:-'admin'}
AUTH_PASS=${AUTH_PASS:-'password'}

htpasswd -b -c /etc/nginx/.htpasswd $AUTH_USER $AUTH_PASS

cp /var/config/nginx/nginx.conf /etc/nginx/nginx.conf
rm -rf /etc/nginx/sites-enabled/*
ln -s /var/config/nginx/default.conf /etc/nginx/sites-enabled/

/usr/sbin/nginx -c /etc/nginx/nginx.conf

exec "$@"
