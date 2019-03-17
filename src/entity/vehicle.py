from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, registration_number, color, vehicle_type):
        self.registration_number = registration_number
        self.color = color
        self.vehicle_type = vehicle_type

    @abstractmethod
    def vehicle_type(self):
        pass
