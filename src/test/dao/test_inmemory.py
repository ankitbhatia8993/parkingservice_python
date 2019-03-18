import unittest

from dao.inmemory import ParkingSlotDao, VehicleDao, VehicleParkingSlotDao
from entity.car import Car
from entity.parking_slot import ParkingSlot
from entity.vehicle_parking_slot import VehicleParkingSlot
from enums.slot_size import SlotSize


class ParkingSlotDaoTest(unittest.TestCase):
    def setUp(self):
        self.parking_slot_dao = ParkingSlotDao()
        self.slot_count = 5

    def get_slots(self):
        expected_slots = []
        for i in range(self.slot_count):
            expected_slots.append(ParkingSlot(SlotSize.MEDIUM.value, _id=i+1))
        return expected_slots

    def test_bulk_create(self):
        expected_slots = self.get_slots()
        self.assertRaises(Exception, self.parking_slot_dao.bulk_create(expected_slots))
        #     return
        # created_slots = self.parking_slot_dao.bulk_create(expected_slots)
        # self.assertEqual(created_slots, expected_slots)

    def test_update(self):
        expected_slot = ParkingSlot(SlotSize.MEDIUM.value, _id=2)
        parking_slot = self.parking_slot_dao.update(expected_slot)
        self.assertEqual(parking_slot, expected_slot)

    def test_get_all(self):
        parking_slots = self.parking_slot_dao.get_all()
        self.assertEqual(parking_slots, self.get_slots())


class VehicleDaoTest(unittest.TestCase):
    def setUp(self):
        self.vehicle_dao = VehicleDao()
        self.color = 'White'
        self.vehicle_number = 'DL-12-AA-9999'

    def get_vehicle(self):
        return Car(self.vehicle_number, self.color)

    def test_create(self):
        vehicle = self.vehicle_dao.create(self.get_vehicle())
        expected_vehicle = self.get_vehicle()
        expected_vehicle.created_on = vehicle.created_on
        self.assertEqual(vehicle, expected_vehicle)

    def test_get(self):
        expected_vehicle = self.get_vehicle()
        vehicle = self.vehicle_dao.get(expected_vehicle.registration_number)
        expected_vehicle.created_on = vehicle.created_on
        self.assertEqual(vehicle, expected_vehicle)

    def test_update(self):
        expected_vehicle = self.get_vehicle()
        vehicle = self.vehicle_dao.update(expected_vehicle)
        expected_vehicle.created_on = vehicle.created_on
        self.assertEqual(vehicle, expected_vehicle)

    def test_get_vehicles_by_color(self):
        expected_vehicles = [self.get_vehicle()]
        vehicles = self.vehicle_dao.get_vehicles_by_color(self.color)
        expected_vehicles[0].created_on = vehicles[0].created_on
        self.assertEqual(vehicles, expected_vehicles)


class VehicleParkingSlotDaoTest(unittest.TestCase):
    def setUp(self):
        self.vehicle_parking_slot_dao = VehicleParkingSlotDao()
        self.vehicle_number = 'DL-12-AA-9999'
        self.slot_number = 2

    def get_vehicle_parking_slot(self):
        return VehicleParkingSlot(self.slot_number, self.vehicle_number, _id=1)

    def test_create(self):
        expected_vehicle_parking_slot = self.get_vehicle_parking_slot()
        vehicle_parking_slot = self.vehicle_parking_slot_dao.create(expected_vehicle_parking_slot)
        expected_vehicle_parking_slot.created_on = vehicle_parking_slot.created_on
        self.assertEqual(vehicle_parking_slot, expected_vehicle_parking_slot)

    def test_get_occupied_slots(self):
        expected_vehicle_parking_slot = self.get_vehicle_parking_slot()
        vehicle_parking_slot = self.vehicle_parking_slot_dao.get_occupied_slots()[0]
        expected_vehicle_parking_slot.created_on = vehicle_parking_slot.created_on
        self.assertEqual(vehicle_parking_slot, expected_vehicle_parking_slot)

    def test_update(self):
        expected_vehicle_parking_slot = self.get_vehicle_parking_slot()
        vehicle_parking_slot = self.vehicle_parking_slot_dao.update(expected_vehicle_parking_slot)
        expected_vehicle_parking_slot.created_on = vehicle_parking_slot.created_on
        self.assertEqual(vehicle_parking_slot, expected_vehicle_parking_slot)

    def test_get_by_parking_slot(self):
        expected_vehicle_parking_slot = self.get_vehicle_parking_slot()
        vehicle_parking_slot = self.vehicle_parking_slot_dao.get_by_parking_slot(self.slot_number)
        expected_vehicle_parking_slot.created_on = vehicle_parking_slot.created_on
        self.assertEqual(vehicle_parking_slot, expected_vehicle_parking_slot)

    def test_get_by_vehicle(self):
        expected_vehicle_parking_slot = self.get_vehicle_parking_slot()
        vehicle_parking_slot = self.vehicle_parking_slot_dao.get_by_vehicle(self.vehicle_number)
        expected_vehicle_parking_slot.created_on = vehicle_parking_slot.created_on
        self.assertEqual(vehicle_parking_slot, expected_vehicle_parking_slot)

    def test_disable_vehicle_parking(self):
        expected_vehicle_parking_slot = self.get_vehicle_parking_slot()
        expected_vehicle_parking_slot.enabled = False
        vehicle_parking_slot = self.vehicle_parking_slot_dao.disable_vehicle_parking(self.slot_number)
        expected_vehicle_parking_slot.created_on = vehicle_parking_slot.created_on
        self.assertEqual(vehicle_parking_slot, expected_vehicle_parking_slot)
        expected_vehicle_parking_slot.enabled = True
        self.vehicle_parking_slot_dao.update(expected_vehicle_parking_slot)


if __name__ == '__main__':
    unittest.main()