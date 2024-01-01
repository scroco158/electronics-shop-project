from src.item import Item


class Kbd_mix:
    """
    Миксин класс придает возможность переключения раскладки клавиатуры
    """
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Функция переключает раскладку клавиатуры
        """

        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, Kbd_mix):
    """
    Класс клавиатура первое наследование от Item в Item добавлен вызов
    инициализатора Kbd_mix
    """
    pass
