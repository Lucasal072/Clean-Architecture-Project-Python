import pytest
from src.entities.user import User
from src.usecases.signin import SignIn
from src.usecases.signup import SignUp
from test.usecases.inmemoryrepo.userrepoinmemory import InMemoryUserRepo
from src.external.bcrypt_hashservice import Bcrypt
from src.usecases.errors.user_exceptions import InvalidCredentialsError, DuplicateUser

repo = InMemoryUserRepo()
crypt = Bcrypt()
signin_service = SignIn(repo, crypt)
signup_service = SignUp(repo, crypt)


def test_user_not_found():
    with pytest.raises(InvalidCredentialsError):
        signin_service.perform("lucas", "teste")


def test_duplicate_user():
    signup_service.perform("pedro", "fehifHIHI7832", 20)
    with pytest.raises(DuplicateUser):
        signup_service.perform("pedro", "frehifGRIHI42332", 35)


def test_user_login():
    signup_service.perform("lucas072", "fejkjofJOOJ302", 20)
    user = signin_service.perform("lucas072", "fejkjofJOOJ302")
    assert user.username == "lucas072"
