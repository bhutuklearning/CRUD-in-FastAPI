# FAST API CRUD Project

This repository contains a full-stack CRUD project:
- `backend/` — FastAPI backend with SQLAlchemy and PostgreSQL/SQLite support
- `frontend/` — React frontend (and future Next.js migration)

## What’s included

### Backend
- FastAPI app with CRUD routes
- SQLAlchemy models and DB session
- Pydantic schemas for request/response validation
- Service layer for business logic
- Environment config support (`.env`)

### Frontend
- React app (set up manually inside `frontend/`)
- Connects to backend endpoints for CRUD operations

## Quick Start

### Backend setup (Windows)
```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# create .env with DATABASE_URL
uvicorn main:app --reload
```

### Frontend setup (React)
```powershell
cd frontend
npm install
npm start
```

## Project structure
```
01_CRUD/
  ├─ backend/
  │   ├─ .env
  │   ├─ main.py
  │   ├─ database.py
  │   ├─ models/item.py
  │   ├─ schemas/item.py
  │   ├─ services/item.py
  │   ├─ routes/item.py
  │   ├─ requirements.txt
  │   └─ README.md
  ├─ frontend/
  │   └─ (React app files)
  └─ Readme.md
```

## Environment variables
Use `.env` in `backend/`:
```env
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
```
For SQLite use:
```env
DATABASE_URL=sqlite:///./test.db
```

##  API Endpoints
Typical CRUD endpoints exposed by `backend/routes/item.py`:
- `GET /items`
- `GET /items/{id}`
- `POST /items`
- `PUT /items/{id}`
- `DELETE /items/{id}`

## Best practices
- Don't commit `.env` or `venv/` (use `.gitignore`).
- Use Alembic for schema migrations when models evolve.
- Keep API contracts in `schemas` and business logic in `services`.

## Notes
- This repo is built for learning FastAPI + React CRUD with a clean, layered architecture.
- You can replace `frontend/` with Next.js later and keep the same API.
