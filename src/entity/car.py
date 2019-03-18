from entity.vehicle import Vehicle
from enums.vehicle_type import VehicleType


class Car(Vehicle):
    def __init__(self, registration_number, color):
        super(Car, self).__init__(registration_number, color, VehicleType.CAR.name)

    def vehicle_type(self):
        return VehicleType.CAR.name

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
