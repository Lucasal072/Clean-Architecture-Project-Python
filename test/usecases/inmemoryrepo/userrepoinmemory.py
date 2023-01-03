from src.usecases.port.interface_user_repo import IUserRepo
from src.entities.user import User


class InMemoryUserRepo(IUserRepo):

    def __init__(self) -> None:
        self.list_user: list[User] = []

    def find_by_username(self, username: str):
        for user in self.list_user:
            if user.username == username:
                return user

    def register_user(self, user: User):
        self.list_user.append(user)
