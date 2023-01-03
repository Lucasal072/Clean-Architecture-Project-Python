from abc import ABC, abstractmethod


class IHashService(ABC):
    @abstractmethod
    def encript(self, password):
        pass

    @abstractmethod
    def check_password(self, password, password_hashed):
        pass
