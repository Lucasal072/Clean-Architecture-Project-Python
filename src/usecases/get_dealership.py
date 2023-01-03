from src.usecases.port.interface_dealership_repo import IDealershipRepo
from src.usecases.errors.dealership_exceptions import NotFoundDealership
from src.entities.dealership import Dealership

class GetDealership:

    def __init__(self,dealership_repo:IDealershipRepo) -> None:
        self.dealership_repo = dealership_repo

    def perform(self,owner_username:str) -> Dealership:
        dealership = self.dealership_repo.find_by_owner_username(owner_username)
        if not dealership:
            raise NotFoundDealership("Dealership not found")
        return dealership
