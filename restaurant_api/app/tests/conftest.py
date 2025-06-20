# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app
from app.dependencies.db import get_db


@pytest.fixture
def mock_db():
    return MagicMock()

@pytest.fixture
def test_client(mock_db):
    app.dependency_overrides[get_db] = lambda: mock_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
