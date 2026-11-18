# LegacyAI — Backend

**Institutional Intelligence Platform.** This is the REST API behind LegacyAI, built with FastAPI and PostgreSQL.

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-SQLAlchemy%202-4169E1?logo=postgresql&logoColor=white)

> **Status:** early development. The service, database layer and user registration are in place; more modules are on the way.

## Tech stack

| Layer | Tool |
|---|---|
| API framework | FastAPI + Uvicorn |
| Database | PostgreSQL |
| ORM | SQLAlchemy 2 |
| Validation | Pydantic 2 (`EmailStr` for email checks) |
| Config | pydantic-settings, read from `.env` |

## API

| Method | Path | What it does |
|---|---|---|
| `GET` | `/` | Health check: returns a welcome message and `"Backend Running"` |
| `POST` | `/users/` | Creates a user from `{ "name", "email" }` and returns `{ "id", "name", "email" }` |

Interactive docs are served at **`/docs`** (Swagger UI) and **`/redoc`** once the server is running.

## Run it locally

You need Python 3.9+ and a running PostgreSQL database.

```bash
git clone https://github.com/adityashukla44/legacyai-backend.git
cd legacyai-backend

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env        # then set DATABASE_URL to your database
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs. The `users` table is created automatically on first start.

## Project structure

```
app/
├── main.py            # FastAPI app, router registration, table creation
├── core/config.py     # Settings loaded from .env
├── database/          # SQLAlchemy engine, session and get_db dependency
├── models/user.py     # User table: id, name, email, password, role, created_at
├── schemas/user.py    # Request / response models
└── routers/
    ├── home.py        # GET /
    └── user.py        # POST /users/
```

## Author

**Aditya Shukla** — [@adityashukla44](https://github.com/adityashukla44)
