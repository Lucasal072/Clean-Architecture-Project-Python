from src.usecases.port.interface_dealership_repo import IDealershipRepo
from src.entities.dealership import Dealership

class InMemoryDealershipRepo(IDealershipRepo):

    def __init__(self) -> None:
        self.list_dealership:list[Dealership] = []

    def find_by_owner_username(self,owner_username:str):
        for dealership in self.list_dealership:
            if dealership.owner.username == owner_username:
                return dealership

    def find_by_name(self,dealership_name:str):
        for dealership in self.list_dealership:
            if dealership.name == dealership_name:
                return dealership
    
    def add_dealership(self,dealership:Dealership):
        self.list_dealership.append(dealership)