from unittest.mock import MagicMock
from uuid import uuid4

def test_create_dish(test_client, mock_db):
    valid_category_id = uuid4()

    fake_category = MagicMock()
    fake_category.id = valid_category_id
    fake_category.name = "Фейковая категория"

    mock_db.query().filter().first.return_value = fake_category
    mock_db.query().filter().all.return_value = []

    mock_db.add.return_value = None
    mock_db.commit.return_value = None

    def fake_refresh(obj):
        obj.id = uuid4()

    mock_db.refresh.side_effect = fake_refresh

    response = test_client.post("/dishes/", json={
        "name": "Мок блюдо",
        "description": "Описание",
        "price": 100.0,
        "category_id": str(valid_category_id)
    })

    print(response.status_code)
    print(response.json())

    assert response.status_code in [200, 201]