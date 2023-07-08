"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item_init(data):
    assert data.name == 'Смартфон'
    assert data.price == 10000
    assert data.quantity == 20


def test_calculate_total_price(data):
    assert data.calculate_total_price() == 200_000


def test_apply_discount(data):
    Item.pay_rate = 0.8
    data.apply_discount()
    assert data.price == 8000.0


def test_name(data):
    data.name = 'Телефон'
    assert data.name == 'Телефон'
    data.name = 'Телефон10000'
    assert data.name == 'Телефон100'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('122.122') == 122
    assert Item.string_to_number('99.9') == 99
