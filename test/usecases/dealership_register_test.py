import pytest
from src.usecases.create_dealership import CreateDealership
from src.entities.user import User
from test.usecases.inmemoryrepo.dealershiprepoinmemory import InMemoryDealershipRepo
from src.usecases.errors.dealership_exceptions import DuplicateDealership, OwnerAlreadyHasADealership


def test_duplicate_name():
    dealearship_repo = InMemoryDealershipRepo()
    c1 = CreateDealership(dealearship_repo)
    u1 = User("Seu lunga", "HJfeie32ijde", 67)
    u2 = User("Seu Jorge", "HJfeie32ijde2", 50)
    c1.perform("Venda de carro do seu lunga", u1)
    with pytest.raises(DuplicateDealership):
        c1.perform("Venda de carro do seu lunga", u2)


def test_owner_already_have_dealership():
    dealearship_repo2 = InMemoryDealershipRepo()
    c1 = CreateDealership(dealearship_repo2)
    u1 = User("Seu Lunga", "HJfeie32ijde", 67)
    u2 = User("Seu Lunga", "HJfeie32ijde2", 50)
    c1.perform("Venda de carro do seu jorge",u1)
    with pytest.raises(OwnerAlreadyHasADealership):
        c1.perform("Venda de carro do seu lunga",u2)

def test_register_dealership():
    dealearship_repo = InMemoryDealershipRepo()
    c1 = CreateDealership(dealearship_repo)
    u1 = User("Seu lunga", "HJfeie32ijde", 67)
    c1.perform("Venda de carro do seu lunga", u1)
    d1 = dealearship_repo.find_by_name("Venda de carro do seu lunga")
    assert d1.owner == u1