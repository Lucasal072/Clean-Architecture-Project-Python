from src.entities.car import Car

class User:
    def __init__(self,username:str,password:str,age:int) -> None:
        self.username = username
        self.password = password
        self.age = age
