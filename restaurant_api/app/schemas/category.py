from pydantic import BaseModel
import uuid

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: uuid.UUID

    class Config:
        from_attributes = True
