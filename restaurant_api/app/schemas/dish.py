from pydantic import BaseModel
from uuid import UUID

class DishBase(BaseModel):
    name: str
    description: str
    price: float
    category_id: UUID

class DishCreate(DishBase):
    pass

class DishRead(DishBase):
    id: UUID

    class Config:
        orm_mode = True
