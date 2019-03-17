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
