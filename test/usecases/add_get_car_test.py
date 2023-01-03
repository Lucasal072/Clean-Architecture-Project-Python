from src.usecases.get_car import GetCar
from src.entities.car import Car
from src.entities.type import TypeCar
from src.entities.dealership import Dealership
from src.usecases.add_car_dealership import AddCar
from src.entities.user import User
from src.usecases.create_car import CreateCar


def test_create_car():
    create_car = CreateCar()
    car = create_car.perform("HJFK345", 2010, "Corsa", TypeCar("popular"))
    assert car.license_plate == "HJFK345"


def test_get_car():
    user = User("lucas", "jfejofJOFEO23", 20)
    dealership = Dealership("Venda de bot do seu lunga", user)
    car = Car("HJFK345", 2010, "Corsa", TypeCar("popular"))
    add_car = AddCar()
    add_car.perform(car, dealership)
    get_car = GetCar()
    d1 = get_car.perform(dealership, license_plate="HJFK345")
    assert d1.license_plate == car.license_plate


def test_add_car():
    user = User("fernando", "jfejofJOFEO23", 32)
    dealership = Dealership("Venda de bot do seu lunga", user)
    car = Car("HJFK345", 2010, "Corsa", TypeCar("popular"))
    add_car = AddCar()
    add_car.perform(car, dealership)
    test_car = dealership.get_list_car(car.license_plate)
    assert test_car.license_plate == car.license_plate
