import pytest

from src.phone import Phone


def test_phone_init(data_for_phone):
    assert data_for_phone.name == 'iPhone 14'
    assert data_for_phone.price == 120000
    assert data_for_phone.quantity == 5
    assert data_for_phone.number_of_sim == 2


def test_sim():
    with pytest.raises(ValueError):
        Phone("iPhone 14", 120_000, 5, 0)
        Phone("iPhone 14", 120_000, 5, -1)
        Phone("iPhone 14", 120_000, 5, 2.5)


def test_phone_str(data_for_phone):
    assert str(data_for_phone) == 'iPhone 14'


def test_phone_repr(data_for_phone):
    assert repr(data_for_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_number_of_sim(data_for_phone):
    assert data_for_phone.number_of_sim == 2

    data_for_phone.number_of_sim = 4
    assert data_for_phone.number_of_sim == 4

    with pytest.raises(ValueError):
        data_for_phone.number_of_sim = 0
        data_for_phone.number_of_sim = -1
        data_for_phone.number_of_sim = 2.5
