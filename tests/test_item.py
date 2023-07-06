"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_item_init(data):
    assert data.name == 'Смартфон'
    assert data.price == 10000
    assert data.quantity == 20


def test_calculate_total_price(data):
    assert data.calculate_total_price() == 200_000


def test_apply_discount(data):
    data.apply_discount()
    assert data.price == 10000.0
