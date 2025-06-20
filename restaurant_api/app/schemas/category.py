from pydantic import BaseModel, ConfigDict
import uuid

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: uuid.UUID
    model_config = ConfigDict(from_attributes=True)
