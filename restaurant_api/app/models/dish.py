import uuid
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base

class Dish(Base):
    __tablename__ = "dishes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"))

    category = relationship("Category", back_populates="dishes")
