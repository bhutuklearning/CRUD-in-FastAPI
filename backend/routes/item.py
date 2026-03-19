from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.item import ItemCreate, ItemResponse
from services import item as item_service
from typing import List

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/", response_model=List[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    return item_service.get_all_items(db)

@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = item_service.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(db, item)

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    updated = item_service.update_item(db, item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

@router.delete("/{item_id}", response_model=ItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted = item_service.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return deleted