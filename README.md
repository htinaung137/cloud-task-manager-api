# Cloud Task Manager API

A cloud-hosted REST API built with Python Flask and PostgreSQL, containerized with Docker Compose, and deployed on AWS EC2 using Nginx and HTTPS.

## Project Overview

This project demonstrates how to develop, containerize, deploy, and operate a database-connected backend application on a Linux cloud server.

## Technologies

| Technology | Purpose |
|---|---|
| Python / Flask | Backend REST API |
| PostgreSQL | Persistent task storage |
| Docker | Application containerization |
| Docker Compose | Multi-container management |
| AWS EC2 / Ubuntu | Cloud hosting |
| Nginx | Reverse proxy |
| DuckDNS | Public domain resolution |
| Certbot / Let's Encrypt | HTTPS certificates |
| GitHub | Source code and version control |

## Architecture

Client → DuckDNS → AWS EC2 → Nginx → Flask → PostgreSQL

The Flask and PostgreSQL services run in separate containers on a Docker Compose network. PostgreSQL data is stored in a persistent Docker volume.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/healthz` | Check API and database health |
| GET | `/tasks` | Retrieve tasks |
| POST | `/tasks` | Create a task |

Task endpoints should be accessed only in an appropriately secured environment.

## Key Learning Outcomes

- Built a Flask REST API using Python.
- Integrated PostgreSQL using Psycopg.
- Created a custom Docker image with a Dockerfile.
- Used Docker Compose to manage multiple services.
- Deployed the application on AWS EC2.
- Configured Nginx reverse proxy routing.
- Connected a DuckDNS hostname and enabled HTTPS.
- Troubleshot port conflicts, Docker startup errors, and Nginx configuration issues.

## Future Improvements

- Add authentication and authorization.
- Implement automated tests.
- Add GitHub Actions CI/CD.
- Configure monitoring and structured logging.
- Improve database migrations and backup procedures.

## Project Status

Initial cloud deployment completed. Security improvements and automated testing are planned.

Japanese

# Cloud Task Manager API

## プロジェクト概要

Python（Flask）とPostgreSQLを使用したタスク管理REST APIを開発し、Docker Composeでコンテナ化してAWS EC2上にデプロイした個人開発プロジェクトです。

Nginxによるリバースプロキシ、DuckDNSによる名前解決、CertbotによるHTTPS通信を構成しました。

## 開発目的

クラウドエンジニアおよびDevOpsエンジニアに必要な、アプリケーション開発からコンテナ化、クラウド環境へのデプロイまでの一連の流れを実践的に理解することを目的としています。

## 使用技術

- バックエンド：Python、Flask
- データベース：PostgreSQL
- コンテナ：Docker、Docker Compose
- クラウド：AWS EC2（Ubuntu）
- Webサーバー：Nginx
- DNS：DuckDNS
- HTTPS：Certbot、Let's Encrypt
- バージョン管理：Git、GitHub

## システム構成

クライアント → DNS → AWS EC2 → Nginx → Flask API → PostgreSQL

## 工夫した点

FlaskとPostgreSQLを別々のコンテナで構築し、Docker Composeの内部ネットワークを利用して通信させました。

また、データベースの永続化にはDocker Volumeを使用し、コンテナを再作成してもデータを保持できる構成にしました。

## 発生した課題と解決方法

**ポート競合**

既存のアプリケーションがポート8080を使用していたため、新しいアプリケーションの起動に失敗しました。Docker Composeのポート設定を見直し、ホスト側のポートを8081に変更することで解決しました。

**Nginxの設定エラー**

シンボリックリンクの参照先ファイルが存在せず、設定テストに失敗しました。設定ファイルを正しい場所に作成し、`nginx -t`で確認してから再読み込みを行いました。

## 今後の改善予定

認証機能、APIの自動テスト、GitHub ActionsによるCI/CD、監視機能などを追加する予定です。
