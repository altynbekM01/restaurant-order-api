from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.database import SessionLocal
from app.models import dish as model
from app.schemas import dish as schema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.DishRead)
def create_dish(dish: schema.DishCreate, db: Session = Depends(get_db)):
    db_dish = model.Dish(**dish.dict())
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish

@router.get("/", response_model=list[schema.DishRead])
def list_dishes(db: Session = Depends(get_db)):
    return db.query(model.Dish).all()
