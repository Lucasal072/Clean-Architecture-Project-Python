from src.usecases.port.interface_user_repo import IUserRepo
from src.usecases.port.interface_hashservice import IHashService
from src.usecases.errors.user_exceptions import InvalidCredentialsError
from src.entities.user import User

class SignIn:
    def __init__(self,user_repo:IUserRepo,hash_service:IHashService):
        self.user_repo = user_repo
        self.hash_service = hash_service

    def perform(self,username:str,password:str):
        user:User = self.user_repo.find_by_username(username)
        if not user or not self.hash_service.check_password(password,user.password):
            raise InvalidCredentialsError("Not Found User or Not check Password")
        return user
