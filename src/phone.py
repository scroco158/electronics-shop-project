# - создайте новый файл `src/phone.py`
# - создайте в `src/phone.py` новый класс `Phone`
# > `Phone` содержит все атрибуты класса `Item` и дополнительно атрибут, содержащий количество поддерживаемых сим-карт
# - реализуйте возможность сложения экземпляров класса `Phone` и `Item` (сложение по количеству товара в магазине)
# > Реализуйте проверки, чтобы нельзя было сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов.

from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        info = super().__repr__()
        info = info[:-1]
        return f'{info}, {self.number_of_sim})'
