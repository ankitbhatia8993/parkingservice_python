from entity.vehicle import Vehicle
from enums.vehicle_type import VehicleType


class Bike(Vehicle):
    def __init__(self, registration_number, color):
        super(Bike, self).__init__(registration_number, color, VehicleType.BIKE.name)

    def vehicle_type(self):
        return VehicleType.BIKE
