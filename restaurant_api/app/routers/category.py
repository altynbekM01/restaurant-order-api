from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import category as model
from app.schemas import category as schema
from app.dependencies.db import get_db
from app.services import crud

router = APIRouter()


@router.post("/", response_model=schema.CategoryRead)
def create_category(category: schema.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_object(db, model.Category, category.dict())


@router.get("/", response_model=list[schema.CategoryRead])
def list_categories(db: Session = Depends(get_db)):
    return crud.list_objects(db, model.Category)


@router.get("/{category_id}", response_model=schema.CategoryRead)
def get_category(category_id: str, db: Session = Depends(get_db)):
    return crud.get_object_or_404(db, model.Category, category_id)


@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: str, db: Session = Depends(get_db)):
    crud.delete_object(db, model.Category, category_id)
