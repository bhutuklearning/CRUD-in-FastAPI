from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):   # what client sends
    name: str
    description: Optional[str] = None

class ItemResponse(BaseModel): # what you send back
    id: int
    name: str
    description: Optional[str]

    class Config:
        from_attributes = True