"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    it1 = Item("it1", 100, 10)
    assert it1.calculate_total_price() == 1000


def test_apply_discount():

    it1 = Item("it1", 100, 10)
    it1.apply_discount()
    assert it1.price == 110
