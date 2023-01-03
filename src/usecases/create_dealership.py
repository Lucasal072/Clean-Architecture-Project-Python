from src.entities.dealership import Dealership
from src.entities.user import User
from src.usecases.errors.user_exceptions import NotUserInstance
from src.usecases.errors.dealership_exceptions import DuplicateDealership,OwnerAlreadyHasADealership
from src.usecases.port.interface_dealership_repo import IDealershipRepo


class CreateDealership:
    def __init__(self, dealerships_repo:IDealershipRepo) -> None:
        self.ds_repo = dealerships_repo

    def perform(self, dealership_name: str, owner: User):
        if not isinstance(owner, User):
            raise NotUserInstance(
                "<param: owner not is instance of User:Class>")
        ds_owner_duplicate = self.ds_repo.find_by_owner_username(owner.username)
        if ds_owner_duplicate:
            raise OwnerAlreadyHasADealership("this owner already have a dealership")
        ds_name_duplicate = self.ds_repo.find_by_name(dealership_name)
        if ds_name_duplicate:
            raise DuplicateDealership("a dealership already have this name")
        dealership = Dealership(dealership_name, owner)
        self.ds_repo.add_dealership(dealership)
        return dealership
