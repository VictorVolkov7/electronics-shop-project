import pytest

from src.item import Item
from src.keyboard import Keyboard
from src.phone import Phone


@pytest.fixture
def data():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def data_for_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def data_for_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)