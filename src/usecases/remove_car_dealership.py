from src.entities.dealership import Dealership
from src.usecases.errors.car_exceptions import NotFoundCar

class RemoveCarDealership:
    
    def perform(self, dealearship:Dealership, license_plate:str):
        car = dealearship.get_list_car(license_plate)
        if not car:
            raise NotFoundCar("Car Not Found")
        dealearship.remove_car(car)