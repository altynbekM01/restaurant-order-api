import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Enum, Table, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.enums import OrderStatus

order_dish = Table(
    "order_dish",
    Base.metadata,
    Column("order_id", UUID(as_uuid=True), ForeignKey("orders.id")),
    Column("dish_id", UUID(as_uuid=True), ForeignKey("dishes.id")),
)

class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_name = Column(String, nullable=False)
    order_time = Column(DateTime, default=datetime.utcnow)
    status = Column(Enum(OrderStatus), default=OrderStatus.processing)

    dishes = relationship("Dish", secondary=order_dish, backref="orders")

    @property
    def total_price(self):
        return sum(dish.price for dish in self.dishes)
