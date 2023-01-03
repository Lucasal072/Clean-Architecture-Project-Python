from src.usecases.signup import SignUp
from test.usecases.inmemoryrepo.userrepoinmemory import InMemoryUserRepo
from src.external.bcrypt_hashservice import Bcrypt
from src.usecases.errors.user_exceptions import InvalidPassword,DuplicateUser
import pytest

def test_wrong_password():
    user_repo = InMemoryUserRepo()
    bcript = Bcrypt()
    s1 = SignUp(user_repo,hash_service=bcript)
    with pytest.raises(InvalidPassword):
        s1.perform("fernando","WRONG-PASSWORD",23)

def test_duplicate_user():
    user_repo = InMemoryUserRepo()
    bcript = Bcrypt()
    s1 = SignUp(user_repo,hash_service=bcript)
    s1.perform("fernando","rgejgeS324okfe",23)
    with pytest.raises(DuplicateUser):
        s1.perform("fernando","rgejgeS32fe4okfe",24)

def test_signup_user():
    user_repo = InMemoryUserRepo()
    bcript = Bcrypt()
    s1 = SignUp(user_repo,hash_service=bcript)
    verify = s1.perform("Pedro","rgejgeS324okfe",23)
    assert verify == True