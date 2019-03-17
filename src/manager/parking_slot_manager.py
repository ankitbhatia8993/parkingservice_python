from dao.inmemory import ParkingSlotDao
from entity.parking_slot import ParkingSlot
from enums.slot_size import SlotSize


class ParkingSlotManager:
    def __init__(self):
        self.parking_slot_dao = ParkingSlotDao()

    def create(self, count, size=SlotSize.MEDIUM.name):
        parking_slots = []
        for i in range(count):
            parking_slot = ParkingSlot(size)
            parking_slots.append(self.parking_slot_dao.create(parking_slot))
        return parking_slots

