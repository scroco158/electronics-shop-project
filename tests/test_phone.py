from src.phone import Phone

def test_init():
    p = Phone('name', 1, 1, 1)
    assert p.name == 'name'
    assert p.price == 1
    assert p.quantity == 1
    assert p.number_of_sim == 1

def test_repr():
    p = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(p) == "Phone('iPhone 14', 120000, 5, 2)"
