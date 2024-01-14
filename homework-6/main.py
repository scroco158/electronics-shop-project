from src.item import Item
import os

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(os.path.abspath('../src/items.csv'))
    # FileNotFoundError: Отсутствует файл item.csv
    print ()
    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(os.path.abspath('../src/items.csv'))
    # InstantiateCSVError: Файл item.csv поврежден
