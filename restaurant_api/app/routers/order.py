from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.database import SessionLocal
from app.models import order as model
from app.models import dish as dish_model
from app.schemas import order as schema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.OrderRead)
def create_order(order_data: schema.OrderCreate, db: Session = Depends(get_db)):
    dishes = db.query(dish_model.Dish).filter(dish_model.Dish.id.in_(order_data.dish_ids)).all()
    if len(dishes) != len(order_data.dish_ids):
        raise HTTPException(status_code=404, detail="One or more dishes not found")

    order = model.Order(customer_name=order_data.customer_name, dishes=dishes)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

@router.get("/", response_model=list[schema.OrderRead])
def list_orders(db: Session = Depends(get_db)):
    return db.query(model.Order).all()
