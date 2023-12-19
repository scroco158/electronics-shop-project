"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import os

def test_calculate_total_price():
    it1 = Item("it1", 100, 10)
    assert it1.calculate_total_price() == 1000


def test_apply_discount():

    it1 = Item("it1", 100, 10)
    it1.apply_discount()
    assert it1.price == 110


def test_setter_getter():
    test_item = Item('0', 100, 100)
    test_item.name = '01234567890123'
    assert test_item.name == '0123456789'


def test_instantiate_from_csv():
    Item.instantiate_from_csv(os.path.abspath('./src/items.csv'))
    assert Item.all[4].name == 'Клавиатура'


def test_string_to_number():
    assert Item.string_to_number('123.123') == 123


def test_repr():
    it = Item("Телевизор", 25000, 10)
    assert repr(it) == "Item('Телевизор', 25000, 10)"


def test_str():
    it = Item("Телевизор", 25000, 10)
    assert str(it) == 'Телевизор'
