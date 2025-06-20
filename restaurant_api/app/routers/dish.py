from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import dish as model
from app.schemas import dish as schema
from app.dependencies.db import get_db
from app.services import crud

router = APIRouter()

@router.post("/", response_model=schema.DishRead)
def create_dish(dish: schema.DishCreate, db: Session = Depends(get_db)):
    return crud.create_object(db, model.Dish, dish.model_dump())

@router.get("/", response_model=list[schema.DishRead])
def list_dishes(db: Session = Depends(get_db)):
    return crud.list_objects(db, model.Dish)

@router.get("/{dish_id}", response_model=schema.DishRead)
def get_dish(dish_id: str, db: Session = Depends(get_db)):
    return crud.get_object_or_404(db, model.Dish, dish_id)

@router.delete("/{dish_id}", status_code=204)
def delete_dish(dish_id: str, db: Session = Depends(get_db)):
    crud.delete_object(db, model.Dish, dish_id)
