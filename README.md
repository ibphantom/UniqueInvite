# Invitational Website

This project is a Flask-based website where users can search for their names against an encrypted list stored in a MariaDB database. If their name matches, they will be redirected to a specific link associated with that name.

## Features
- Name search feature with encryption
- Flask backend with a MariaDB database connection
- Dual licensing (MIT for open-source use and Commercial License for proprietary use)

## Setup

### Prerequisites
- Docker
- MariaDB instance

### Running Locally
You can run this project locally using Docker:

```bash
docker build -t your-app-image .
docker run -p 5000:5000 --env MYSQL_HOST=mariadb --env MYSQL_USER=root --env MYSQL_PASSWORD=your_password --env MYSQL_DATABASE=your_database your-app-image
