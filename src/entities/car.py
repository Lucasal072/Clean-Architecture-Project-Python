from src.entities.type import TypeCar


class Car:
    value_sell = 0
    value_buy = 0

    def __init__(self, license_plate: str, year: int, name: str, types:TypeCar) -> None:
        self.license_plate = self.set_license_plate(license_plate)
        self.age = year
        self.name = name
        self.type = self.set_type_car(types)

    def __repr__(self) -> str:
        return f"{self.name}-{self.age} license_plate = {self.license_plate}"

    def set_license_plate(self, license_plate: str) -> str:
        if len(license_plate) == 7:
            return license_plate

    def get_license_plate(self) -> str:
        return self.license_plate

    def set_type_car(self, type: str) -> None:
        self.type = TypeCar(type)

    def get_type_car(self) -> str:
        return self.type

    def set_value_sell(self, value:int) -> None:
        self.value_sell = value
    
    def get_value_sell(self) -> int:
        return self.value_sell
    
    def set_value_buy(self, value:int) -> None:
        self.value_buy = value
    
    def get_value_buy(self) -> int:
        return self.value_buy
    
