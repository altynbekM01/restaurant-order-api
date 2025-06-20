# 🍽️ Restaurant API

**FastAPI-проект для управления заказами и меню ресторана**

## 📌 Описание

REST API-сервис позволяет:

- управлять меню (категории, блюда),
- создавать, просматривать и отменять заказы,
- менять статус заказа.

## 📦 Функциональность

- Модели:
  - **Category** — категория блюда
  - **Dish** — блюдо
  - **Order** — заказ
  - **OrderStatus** — статус заказа (`Enum`)
- Поддерживаются операции **Create**, **Read**, **Delete** для всех моделей.
- Отдельный endpoint:
  - `PATCH /orders/{id}/status` — изменение статуса заказа.

## 🔄 Бизнес-логика

- При создании заказа проверяется, что все блюда существуют.
- Заказ можно отменить **только в статусе `в обработке`**.
- Статусы изменяются **последовательно**:  
  `в обработке → готовится → доставляется → завершен`.

## 🧰 Технологии

- ⚡ **FastAPI** — основной фреймворк
- 🐘 **PostgreSQL** — база данных
- 🛠️ **SQLAlchemy** — работа с БД
- 🔄 **Alembic** — миграции
- 🐳 **Docker + docker-compose** — контейнеризация
- 🧪 **pytest** — тесты (POST для блюда и заказа)
- 📁 Модульная структура проекта:  
  `routers/`, `models/`, `schemas/`, `services/`, `tests/`

## 🚀 Запуск

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/restaurant-api.git
   cd restaurant-api
   
2.  Создайте .env на основе .env.example (Илм можете взять этот пример)
    
    POSTGRES_DB=restaurant_db
    POSTGRES_USER=restaurant_user
    POSTGRES_PASSWORD=your_password
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    
    
3.  Запустите проект:
    ```
    docker-compose up --build -d

4.  Проведите миграции:
    ```
    docker-compose exec web alembic revision --autogenerate -m "init tables"
    docker-compose exec web alembic upgrade head

Тесты

    docker-compose exec web pytest
