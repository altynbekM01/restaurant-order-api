from uuid import uuid4
from unittest.mock import MagicMock
from datetime import datetime, UTC

def test_create_order(test_client, mock_db):
    fake_dish_id = uuid4()
    fake_dish = MagicMock()
    fake_dish.id = fake_dish_id
    fake_dish.name = "Мок-блюдо"
    fake_dish.description = "Описание"
    fake_dish.price = 100.0
    fake_dish.category_id = uuid4()

    mock_db.query().filter().all.return_value = [fake_dish]
    mock_db.query().filter().first.return_value = fake_dish

    mock_db.add.return_value = None
    mock_db.commit.return_value = None

    def fake_refresh(obj):
        obj.id = uuid4()
        obj.dishes = [fake_dish]
        obj.order_time = datetime.now(UTC)
        obj.status = "в обработке"

    mock_db.refresh.side_effect = fake_refresh

    response = test_client.post("/orders/", json={
        "customer_name": "Тест Заказчик",
        "dish_ids": [str(fake_dish_id)]
    })

    print(response.status_code)
    print(response.json())

    assert response.status_code in [200, 201]
    assert "id" in response.json()
    assert response.json()["customer_name"] == "Тест Заказчик"
    assert isinstance(response.json()["dishes"], list)
