from garage import Garage
from models import Bus, Car, Motorcycle, Truck


def main():
    vehicles = [
        Car("Toyota", "Camry", 2024, 4),
        Truck("КАМАЗ", "54901", 2022, 20),
        Motorcycle("Yamaha", "MT-07", 2021, False),
        Bus("ЛиАЗ", "5292", 2023, 110, 144),
    ]

    print("Движение транспорта:")
    for vehicle in vehicles:
        vehicle.accelerate(60)
        print("-", vehicle.move())

    garage = Garage()
    for vehicle in vehicles:
        garage.add_vehicle(vehicle)
    garage.show_all()

    print("Поиск по марке ЛиАЗ:")
    for vehicle in garage.find_by_brand("ЛиАЗ"):
        print("-", vehicle)


if __name__ == "__main__":
    main()
