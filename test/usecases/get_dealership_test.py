from src.usecases.create_dealership import CreateDealership
from src.usecases.get_dealership import GetDealership
from src.entities.user import User
from test.usecases.inmemoryrepo.dealershiprepoinmemory import InMemoryDealershipRepo
from src.usecases.errors.dealership_exceptions import NotFoundDealership
import pytest




def test_not_found_dealership():
    repo = InMemoryDealershipRepo()
    c1 = CreateDealership(repo)
    g1 = GetDealership(repo)
    u1 = User("Lucas0832", "feijfjieJIFEJI8943", 32)
    c1.perform("Vendas de Carros", u1)
    with pytest.raises(NotFoundDealership):
        g1.perform("Lucas08343")


def test_get_dealership():
    repo = InMemoryDealershipRepo()
    c1 = CreateDealership(repo)
    g1 = GetDealership(repo)
    u1 = User("Lucas0832", "feijfjieJIFEJI8943", 32)
    c1.perform("Vendas de Carros", u1)
    dealership = g1.perform("Lucas0832")
    assert dealership.owner.username == "Lucas0832"