import csv
import os.path


class InstantiateCSVError(Exception):

    def __init__(self, *args, ** kwargs):
        self.message = args[0] if args else 'File problem'

    def __str__(self):
        return self.message

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.1
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__) or issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = round(self.price * self.pay_rate)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, filename):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        if os.path.isfile(filename):
            cls.all = []
            with open(filename, newline='', encoding='Windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) == 3:
                        name = row['name']
                        price = row['price']
                        quantity = row['quantity']
                        cls(name, float(price), int(quantity))
                    else:
                        raise InstantiateCSVError('_Файл item.csv поврежден_')
        else:
            raise FileNotFoundError('_Отсутствует файл item.csv_')
    @staticmethod
    def string_to_number(string_to_convert):
        """
        Cтатический метод, возвращающий число из числа-строки
        """
        return int(float(string_to_convert))
