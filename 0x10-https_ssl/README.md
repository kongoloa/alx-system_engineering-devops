# 0x10. HTTPS SSL

## Table of contents
Files | Description
----- | -----------
[0-world_wide_web](./0-world_wide_web) | Configures domain zone so that the subdomain www points to load-balancer IP (lb-01).
[1-haproxy_ssl_termination](./1-haproxy_ssl_termination) Configures HAproxy to accept encrypted traffic for subdomain "www."
[100-redirect_http_to_https](./100-redirect_http_to_https) | Configures HAproxy to automatically redirect HTTP traffic to HTTPS
