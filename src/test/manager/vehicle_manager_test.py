import unittest

from entity.car import Car
from manager.vehicle_manager import VehicleManager


class VehicleManagerTest(unittest.TestCase):
    def setUp(self):
        self.vehicle_manager = VehicleManager()
        self.color = 'White'
        self.vehicle_number = 'DL-12-AA-9999'

    def get_vehicle(self):
        return Car(self.vehicle_number, self.color)

    def test_create(self):
        expected_vehicle = self.get_vehicle()
        vehicle = self.vehicle_manager.create(self.vehicle_number, self.color)
        expected_vehicle.created_on = vehicle.created_on
        self.assertEqual(vehicle, expected_vehicle)

    def test_get(self):
        expected_vehicle = self.get_vehicle()
        vehicle = self.vehicle_manager.get(expected_vehicle.registration_number)
        expected_vehicle.created_on = vehicle.created_on
        self.assertEqual(vehicle, expected_vehicle)

    def test_get_vehicles_by_color(self):
        expected_vehicles = [self.get_vehicle()]
        vehicles = self.vehicle_manager.get_vehicles_by_color(self.color)
        expected_vehicles[0].created_on = vehicles[0].created_on
        self.assertEqual(vehicles, expected_vehicles)
