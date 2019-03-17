from dao.inmemory import VehicleDao
from entity.bike import Bike
from entity.car import Car
from enums.vehicle_type import VehicleType


class VehicleManager:
    def __init__(self):
        self.vehicle_dao = VehicleDao()

    def create(self, registration_number, color, vehicle_type=VehicleType.CAR):
        vehicle = {
            VehicleType.CAR: Car(registration_number, color),
            VehicleType.BIKE: Bike(registration_number, color)
        }.get(vehicle_type)
        return self.vehicle_dao.create(vehicle)

    def get(self, registration_number):
        return self.vehicle_dao.get(registration_number)

    def get_vehicles_by_color(self, color, printing=False):
        vehicles = self.vehicle_dao.get_vehicles_by_color(color)
        if printing:
            print(', '.join([vehicle.registration_number for vehicle in vehicles]))
        return vehicles

