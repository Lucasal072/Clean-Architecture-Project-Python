from typing import Union
from src.entities.car import Car
from src.entities.user import User

class Dealership:
    
    def __init__(self,name:str,owner:User) -> None:
        self.name = name
        self.owner = owner
        self.list_car:list[Car] = []

    def set_list_car(self,list_car:list[Car]):
        self.list_car:list[Car] = list_car
    
    def get_list_car(self,license_plate:str=None) -> Union[list[Car],Car]:
        if license_plate is not None:
            for car in self.list_car:
                if car.license_plate == license_plate:
                    return car
        else:
            return self.list_car

    def add_car(self,car:Car):
        self.list_car.append(car)
    
    def remove_car(self,car:Car):
        self.list_car.remove(car)

