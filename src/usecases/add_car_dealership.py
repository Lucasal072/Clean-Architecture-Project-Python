from src.entities.car import Car
from src.entities.dealership import Dealership
from src.usecases.errors.car_exceptions import DuplicateLicensePlate


class AddCar:
    def perform(self,car:Car,dealearship:Dealership):
        duplicate_car = dealearship.get_list_car(car.license_plate)
        if duplicate_car:
            raise DuplicateLicensePlate("already have a car with this license plate")
        dealearship.add_car(car)