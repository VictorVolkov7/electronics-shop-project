import pytest
from src.item import Item


@pytest.fixture
def data():
    return Item("Смартфон", 10000, 20)
