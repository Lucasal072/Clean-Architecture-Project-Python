from src.usecases.remove_car_dealership import RemoveCarDealership
from src.entities.dealership import Dealership
from src.entities.user import User
from src.entities.type import TypeCar
from src.entities.car import Car

def test_remove_car():
    car = Car("FEHJ323",2020,"Argo",TypeCar("popular"))
    user = User("victor","jfeifji2342FEF",19)
    dealership = Dealership("eu vendo carros",user)
    dealership.add_car(car)
    print(dealership.list_car)
    remove_car = RemoveCarDealership()
    remove_car.perform(dealership,"FEHJ323")