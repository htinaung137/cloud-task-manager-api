
flowchart TB
    User["Browser / API Client"]
    DNS["DuckDNS — Domain to EC2 IP"]

    User -. "DNS lookup" .-> DNS
    DNS -. "Returns public IP" .-> User

    subgraph EC2["AWS EC2 — Ubuntu"]
        Nginx["Nginx — HTTPS :443
        TLS certificate from Let's Encrypt"]

        subgraph Docker["Docker Compose"]
            Flask["Flask API + Gunicorn
            backend :8080"]
            DB["PostgreSQL
            db :5432"]
            Volume[("Persistent Docker Volume")]

            Flask -->|"SQL via Docker network"| DB
            DB --- Volume
        end

        Nginx -->|"127.0.0.1:8081 → :8080"| Flask
    end

    User -->|"HTTPS request"| Nginx

    classDef frontend fill:#e5f0ff,stroke:#3577c8,color:#173b6c
    classDef api fill:#e5f0ff,stroke:#3577c8,color:#173b6c
    classDef database fill:#e4f5e9,stroke:#32955c,color:#205c37
    class User,DNS frontend
    class Nginx,Flask api
    class DB,Volume database
