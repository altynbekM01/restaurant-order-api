from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.database import SessionLocal
from app.models import category as model
from app.schemas import category as schema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.CategoryRead)
def create_category(category: schema.CategoryCreate, db: Session = Depends(get_db)):
    db_category = model.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/", response_model=list[schema.CategoryRead])
def list_categories(db: Session = Depends(get_db)):
    return db.query(model.Category).all()
