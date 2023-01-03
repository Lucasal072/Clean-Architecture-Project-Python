from src.entities.car import Car
from src.entities.type import TypeCar


def test_set_value_car():
    c1 = Car("HJFK784", 2004, "Corsa", TypeCar("popular"))
    c1.set_value_buy(10000)
    assert c1.get_value_buy() == 10000
