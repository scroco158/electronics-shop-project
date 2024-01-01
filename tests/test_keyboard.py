from src.keyboard import Keyboard


def test_change_lang():
    k1 = Keyboard('K', 150, 50)

    assert k1.language == 'EN'
    assert k1.name == 'K'
    assert k1.price == 150.0
    assert k1.quantity == 50

    k1.change_lang()

    assert k1.language == 'RU'




