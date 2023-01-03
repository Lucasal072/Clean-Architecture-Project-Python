from src.usecases.port.interface_user_repo import IUserRepo
from src.usecases.port.interface_hashservice import IHashService
from src.usecases.errors.user_exceptions import DuplicateUser, InvalidPassword
from src.entities.user import User


class SignUp:
    def __init__(self, user_repo: IUserRepo, hash_service: IHashService):
        self.user_repo = user_repo
        self.hash_service = hash_service

    def perform(self, username: str, password: str, age: int):
        duplicate_verify_user = self.user_repo.find_by_username(username)
        if duplicate_verify_user:
            raise DuplicateUser("already have a user with this username")
        if not self.valid_password(password):
            raise InvalidPassword(
                "your password need 8 or more lenght and one lowercase letter, one uppercase letter, one number")
        password_hashed = self.hash_service.encript(password)
        user = User(username, password_hashed, age)
        self.user_repo.register_user(user)
        return True

    def valid_password(self, password: str):
        if len(password) < 8:
            return False
        if not self.verify_password_strength(password):
            return False
        return True

    def verify_password_strength(self, string: str):
        password_strength = 0
        list_propertys = ["islower", "isupper", "isdecimal"]
        for propertys in list_propertys:
            for l in string:
                if getattr(l, propertys)():
                    password_strength += 1
                    break
        if password_strength >= 3:
            return True
