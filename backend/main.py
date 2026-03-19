from fastapi import FastAPI
from database import Base, engine
from routes.item import router as item_router

Base.metadata.create_all(bind=engine)  # creates tables if they don't exist

app = FastAPI(title="FastAPI CRUD")

@app.get("/home")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD application!"}

app.include_router(item_router)