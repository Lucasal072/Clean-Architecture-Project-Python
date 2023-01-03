from src.entities.car import Car
from src.entities.dealership import Dealership
from src.usecases.errors.car_exceptions import NotFoundCar


class GetCar:
    def perform(self, dealership:Dealership, license_plate:str) -> Car:
        car:Car = dealership.get_list_car(license_plate)
        if not car:
            raise NotFoundCar
        return car