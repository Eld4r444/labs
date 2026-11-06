class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
        else:
            print("Этого транспортного средства нет в гараже")

    def show_all(self):
        print("Транспорт в гараже:", len(self.vehicles))
        for number, vehicle in enumerate(self.vehicles, start=1):
            print(f"{number}. {vehicle.get_info()}")

    def find_by_brand(self, brand):
        return [
            vehicle for vehicle in self.vehicles
            if vehicle.brand.lower() == brand.lower()
        ]
