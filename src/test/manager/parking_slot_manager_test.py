import unittest

from entity.parking_slot import ParkingSlot
from enums.slot_size import SlotSize
from manager.parking_slot_manager import ParkingSlotManager


class ParkingSlotManagerTest(unittest.TestCase):
    def setUp(self):
        self.parking_slot_manager = ParkingSlotManager()
        self.slot_count = 5

    def get_slots(self):
        expected_slots = []
        for i in range(self.slot_count):
            expected_slots.append(ParkingSlot(SlotSize.MEDIUM.value, _id=i+1))
        return expected_slots

    def test_create(self):
        expected_slots = self.get_slots()
        created_slots = self.parking_slot_manager.create(self.slot_count)
        self.assertEqual(created_slots, expected_slots)

    def test_get_all(self):
        parking_slots = self.parking_slot_manager.get_all()
        self.assertEqual(parking_slots, self.get_slots())
