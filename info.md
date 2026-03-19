# FastAPI CRUD Project Plan

A simple FastAPI backend with a React frontend (migrate to Next.js later).

## 1) Setup (Windows)
1. Create venv:
   ```powershell
   python -m venv venv
   ```
2. Activate venv:
   ```powershell
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv alembic
   ```
4. Freeze requirements:
   ```powershell
   pip freeze > backend\requirements.txt
   ```

## 2) Dependency Purpose
| Package | Purpose |
|---|---|
| `fastapi` | Web framework for API endpoints |
| `uvicorn` | ASGI server to run FastAPI app |
| `sqlalchemy` | ORM for models and DB queries |
| `psycopg2-binary` | PostgreSQL driver for SQLAlchemy |
| `python-dotenv` | Load environment variables from `.env` |
| `alembic` | Manage DB migrations and schema changes |

## 3) Project Structure (Backend)
```
backend/
  ├─ .env                # local secrets (never commit)
  ├─ .gitignore          # ignores for Python backend
  ├─ main.py             # FastAPI app startup
  ├─ database.py         # SQLAlchemy engine and session
  ├─ requirements.txt    # pinned dependencies
  ├─ models/
  │   └─ item.py         # SQLAlchemy model definitions
  ├─ schemas/
  │   └─ item.py         # Pydantic request/response schemas
  ├─ services/
  │   └─ item.py         # business logic layer
  └─ routes/
      └─ item.py         # CRUD API endpoints
```

## 4) Quick Run
```powershell
cd backend
venv\Scripts\activate
uvicorn main:app --reload
```

## 5) Notes
- Keep secrets out of Git by adding `.env` and `venv/` to `.gitignore`.
- Use `alembic` later for migrations when model schema changes.
- Build React frontend in `frontend/`, then integrate with backend API calls.
