from dao.cache import Cache
from dao.inmemory import ParkingSlotDao
from entity.parking_slot import ParkingSlot
from enums.slot_size import SlotSize


class ParkingSlotManager:
    def __init__(self):
        self.parking_slot_dao = ParkingSlotDao()
        self.cache = Cache.get_instance()

    def create(self, count, size=SlotSize.MEDIUM.name):
        parking_slots = []
        for i in range(count):
            parking_slots.append(ParkingSlot(size))
        parking_slots = self.parking_slot_dao.bulk_create(parking_slots)
        for parking_slot in parking_slots:
            self.cache.add_slot(parking_slot.id)
        print('Created a parking lot with %d slots' % count)
        return parking_slots

