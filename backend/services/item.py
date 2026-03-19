from sqlalchemy.orm import Session
from models.item import Item
from schemas.item import ItemCreate

def get_all_items(db: Session):
    return db.query(Item).all()

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, item: ItemCreate):
    new_item = Item(**item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_item(db: Session, item_id: int, item: ItemCreate):
    db_item = get_item(db, item_id)
    if not db_item:
        return None
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item