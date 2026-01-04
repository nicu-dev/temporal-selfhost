### About

This setup spins up a **Temporal cluster** secured with SSL on your local network. It utilizes **Traefik** and the **DNS-01 challenge** to automatically provision and manage Let's Encrypt certificates for your local services.

#### Setup Requirements

To enable the Traefik DNS-01 challenge, you need to provide credentials for your DNS provider.

1. Create a folder named `letsencrypt` in the project root.
2. Add your provider's required credential files to that folder. For example, if you are using **Cloudflare**, you will need:
   - `CF_EMAIL.txt`
   - `CF_KEY.txt`

#### Project Structure

```text
.
├── letsencrypt/
│   ├── CF_EMAIL.txt
│   └── CF_KEY.txt
├── docker-compose.yml
└── ...
```
