from src.entities.car import Car
from src.entities.type import TypeCar
from typing import Union, Literal


class CreateCar:

    def perform(self, license_plate: str, year: int, name: str, type_name: Union[Literal["esportivo"], Literal["popular"], Literal["luxuoso"]]):
        type = TypeCar(type_name)
        car = Car(license_plate, year, name, type)
        return car