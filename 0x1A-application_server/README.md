# 0x1A. Application server

## Table of contents
File | Description
---- | -----------
[2-app_server-nginx_config](./2-app_server-nginx_config) | configure Nginx to serve your page from the route /airbnb-onepage
[3-app_server-nginx_config](./3-app_server-nginx_config) | Nginx config file setup to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001
[4-app_server-nginx_config](./4-app_server-nginx_config) | Nginx config file setup so that the route /api/ points to a Gunicorn instance listening on port 5002
[5-app_server-nginx_config](./5-app_server-nginx_config) | Nginx config file  so that it properly serves the static assets found in web_dynamic/static/ and so that the route / points to your Gunicorn instance
[gunicorn.service](./gunicorn.service) | A systemd script which starts a Gunicorn process to serve the same content as the previous task (web_dynamic/2-hbnb.py)
[4-reload_gunicorn_no_downtime](./4-reload_gunicorn_no_downtime) | A simple Bash script to reload Gunicorn in a graceful way
