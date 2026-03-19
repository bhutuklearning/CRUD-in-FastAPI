# FastAPI CRUD Backend

A simple FastAPI backend for item CRUD operations.

## Project Structure

```
backend/
  ├─ .env                  # local environment variables (not committed)
  ├─ .gitignore            # Python and local ignores
  ├─ main.py               # FastAPI app entrypoint
  ├─ database.py           # database engine and session setup
  ├─ requirements.txt      # Python dependencies
  ├─ models/item.py        # SQLAlchemy model(s)
  ├─ schemas/item.py       # Pydantic request/response schemas
  ├─ services/item.py      # CRUD business logic
  └─ routes/item.py        # API route definitions
```

## Quick Start (Windows)

1. Open terminal in `backend/`
2. Create and activate venv:
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Create `.env` with your database settings (example below).
5. Run the app:
   ```powershell
   uvicorn main:app --reload
   ```

## Example `.env`

```
DATABASE_URL=postgresql://username:password@localhost:5432/mydb
```

If you use SQLite locally, set:
```
DATABASE_URL=sqlite:///./test.db
```

## Endpoints

Assuming default router prefix (e.g. `/items`), your API supports:
- `GET /items` - List all items
- `GET /items/{id}` - Get one item by ID
- `POST /items` - Create new item
- `PUT /items/{id}` - Update item by ID
- `DELETE /items/{id}` - Delete item by ID

## How the project works

- `main.py` starts the FastAPI app and includes routes
- `database.py` configures SQLAlchemy engine and session
- `models/item.py` defines ORM model (DB table)
- `schemas/item.py` defines Pydantic models for request/response validation
- `services/item.py` contains business logic and database operations
- `routes/item.py` maps HTTP endpoints to service functions

##  Tips
- Keep `.env` secret and out of source control.
- Use `alembic` for migrations when model schemas change.
- For local development, use `uvicorn main:app --reload`.

##  Next steps
1. Build React frontend in `frontend/` and call backend endpoints.
2. Add unit tests for service and route logic.
3. Add OpenAPI docs and request validation improvements.
