from parking_lot.src.entity.vehicle import Vehicle
from parking_lot.src.enum.vehicle_type import VehicleType


class Car(Vehicle):
    def __init__(self, registration_number, color):
        super(Car, self).__init__(registration_number, color, VehicleType.CAR.name)

    def vehicle_type(self):
        return VehicleType.CAR.name
