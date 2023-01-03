from abc import ABC,abstractmethod
from src.entities.dealership import Dealership

class IDealershipRepo(ABC):
    @abstractmethod
    def find_by_owner_username(self,owner_name:str):
        pass
    @abstractmethod
    def find_by_name(self,dealership_name:str):
        pass
    @abstractmethod
    def add_dealership(self,dealership:Dealership):
        pass
