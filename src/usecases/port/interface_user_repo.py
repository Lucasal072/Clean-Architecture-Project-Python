from abc import ABC,abstractmethod
from src.entities.user import User

class IUserRepo(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def find_by_username(username:str):
        pass

    @abstractmethod
    def register_user(user:User):
        pass