from src.entities.dealership import Dealership
from src.entities.user import User
from src.entities.car import Car
from src.entities.type import TypeCar


def test_add_car():
    u1 = User("lucas", 20, "12345675424")
    d1 = Dealership(name="Venda de Carros do seu lunga", owner=u1)
    c1 = Car("HJIK324", 2010, "Corsa", TypeCar("popular"))
    d1.set_list_car([])
    d1.add_car(c1)
    car = d1.get_list_car(license_plate="HJIK324")
    assert car == c1
    


def test_remove_car():
    u1 = User("lucas", 20, "12345675424")
    d1 = Dealership(name="Venda de Carros do seu lunga", owner=u1)
    c1 = Car("HJIK324", 2010, "Corsa", TypeCar("popular"))
    d1.add_car(c1)
    d1.remove_car(c1)
    car = d1.get_list_car("HJIK324")
    assert car == None
