from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
from typing import Type, TypeVar

T = TypeVar("T")


def create_object(db: Session, model_class: Type[T], data: dict) -> T:
    obj = model_class(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_object_or_404(db: Session, model_class: Type[T], obj_id) -> T:
    obj = db.query(model_class).get(obj_id)
    if not obj:
        raise HTTPException(status_code=404, detail=f"{model_class.__name__} not found")
    return obj


def list_objects(db: Session, model_class: Type[T]) -> list[T]:
    return db.query(model_class).all()


def delete_object(db: Session, model_class: Type[T], obj_id) -> None:
    obj = get_object_or_404(db, model_class, obj_id)
    db.delete(obj)
    db.commit()
