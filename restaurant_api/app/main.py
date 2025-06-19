from fastapi import FastAPI
from app.routers import dish, category, order

app = FastAPI(title="Restaurant API")


app.include_router(dish.router, prefix="/dishes", tags=["Dishes"])
app.include_router(category.router, prefix="/categories", tags=["Categories"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])
