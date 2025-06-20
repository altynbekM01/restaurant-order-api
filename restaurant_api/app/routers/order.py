from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import order as model
from app.models import dish as dish_model
from app.schemas import order as schema
from app.dependencies.db import get_db
from app.services import crud

router = APIRouter()


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
    return crud.list_objects(db, model.Order)


@router.get("/{order_id}", response_model=schema.OrderRead)
def get_order(order_id: str, db: Session = Depends(get_db)):
    return crud.get_object_or_404(db, model.Order, order_id)


@router.delete("/{order_id}", status_code=204)
def delete_order(order_id: str, db: Session = Depends(get_db)):
    order = crud.get_object_or_404(db, model.Order, order_id)

    if order.status != "в обработке":
        raise HTTPException(status_code=400, detail="Удалить можно только заказ в статусе 'в обработке'")

    db.delete(order)
    db.commit()


@router.patch("/{order_id}/status", response_model=schema.OrderRead)
def update_order_status(order_id: str, new_status: schema.OrderStatusUpdate, db: Session = Depends(get_db)):
    order = crud.get_object_or_404(db, model.Order, order_id)

    allowed_transitions = {
        "в обработке": ["готовится", "отменен"],
        "готовится": ["доставляется"],
        "доставляется": ["завершен"],
    }

    current = order.status
    target = new_status.status

    if target not in allowed_transitions.get(current, []):
        raise HTTPException(status_code=400, detail=f"Недопустимый переход из '{current}' в '{target}'")

    order.status = target
    db.commit()
    db.refresh(order)
    return order
