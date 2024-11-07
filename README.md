# Message Persistence Service

This project is a Flask-based message persistence service designed to archive messages for an AI assistant system. The service exposes a REST API and is integrated with a PostgreSQL database using SQLAlchemy. 

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Docker Setup](#docker-setup)
  - [Local Setup](#local-setup)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [License](#license)

## Features

- **Message persistence**: Stores messages in a PostgreSQL database.
- **REST API**: Provides endpoints to create, update, and retrieve messages.
- **JWT Authentication**: Secures endpoints using JWT tokens.
- **Dockerized Setup**: Uses Docker and Docker Compose for easy deployment.

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.9+ if running locally

## Setup

### Docker Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/shokace/assignment1.git
    cd assignment1
    ```

2. Create a `.env` file in the root directory and define the necessary environment variables:
    ```env
    DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/database_as1
    JWT_SECRET_KEY=your_secret_key
    ```

3. Build and start the service using Docker Compose:
    ```bash
    docker-compose up --build
    ```

4. The service should now be running on `http://localhost:5000`.

### Local Setup

If you'd like to run the app locally without Docker:

1. Clone this repository:
    ```bash
    git clone https://github.com/shokace/assignment1.git
    cd assignment1
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and define the necessary environment variables:
    ```env
    DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/database_as1
    JWT_SECRET_KEY=your_secret_key
    ```

5. Run the application:
    ```bash
    flask run
    ```

The service will be accessible at `http://localhost:5000`.

## Environment Variables

Define the following environment variables in your `.env` file:

- `DATABASE_URL`: Connection string for the PostgreSQL database.
- `JWT_SECRET_KEY`: Secret key used for JWT token generation.

## API Endpoints

| Endpoint           | Method | Description                   |
|--------------------|--------|-------------------------------|
| `/messages`        | POST   | Create a new message          |
| `/messages/<id>`   | PUT    | Update an existing message    |
| `/messages`        | GET    | Retrieve all messages         |

### Sample JSON Body

```json
{
  "message_id": "99457155-71b3-4613-9bdd-da0ce9b3def8",
  "chat_id": "123e4567-e89b-12d3-a456-426614174000",
  "content": "Hello, this is a test message",
  "rating": true,
  "sent_at": "2024-11-07T14:00:00Z",
  "role": "user"
}
