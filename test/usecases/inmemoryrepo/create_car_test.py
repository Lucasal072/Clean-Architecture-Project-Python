from src.usecases.create_car import CreateCar

def test_create_car():
    create_car = CreateCar()
    car = create_car.perform("hjfk345",2010,"Corsa","popular")
    assert car.license_plate == "hjfk345"