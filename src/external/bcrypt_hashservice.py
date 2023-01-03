# from src.usecases.port.interface_hashservice import IHashService
from bcrypt import hashpw, checkpw, gensalt


class Bcrypt:

    def encript(self, password: str) -> str:
        hashed_password = hashpw(password.encode(), gensalt())
        return hashed_password

    def check_password(self, password: str, password_hashed: str) -> bool:
        if checkpw(password.encode(), password_hashed):
            return True
        else:
            return False
