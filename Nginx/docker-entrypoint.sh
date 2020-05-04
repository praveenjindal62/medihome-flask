#!/usr/bin/env sh
set -eu

envsubst '${APPURL} ${APPPORT}' < /etc/nginx/conf.d/nginx.conf.template > /etc/nginx/conf.d/default.conf

exec "$@"
