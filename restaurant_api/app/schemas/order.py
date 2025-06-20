from pydantic import BaseModel, ConfigDict
from typing import List
from uuid import UUID
from datetime import datetime
from app.models.enums import OrderStatus
from app.schemas.dish import DishRead

class OrderBase(BaseModel):
    customer_name: str

class OrderCreate(OrderBase):
    dish_ids: List[UUID]

class OrderRead(OrderBase):
    id: UUID
    order_time: datetime
    status: OrderStatus
    dishes: List[DishRead]
    total_price: float

    model_config = ConfigDict(from_attributes=True)

class OrderStatusUpdate(BaseModel):
    status: OrderStatus
    model_config = ConfigDict(from_attributes=True)