from typing import Optional

from pydantic import BaseModel, ConfigDict
from uuid import UUID

class DishBase(BaseModel):
    name: str
    description: str
    price: float
    category_id: Optional[UUID]

class DishCreate(DishBase):
    pass

class DishRead(DishBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)
