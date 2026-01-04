### About

Spins up a temporal cluster, SSL-ed on local network via traefik dns01 challenge.

For traefik dns01 challenge to work, create root folder `letsencrypt`, and add the traefik required files for your DNS provider (e.g Cloudflare: CF_EMAIL.txt and CF_KEY.txt).

./letsencrypt/
|
|---CF_EMAIL.txt
|---CF_KEY.txt
