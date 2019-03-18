from dao.cache import Cache
from dao.inmemory import ParkingSlotDao
from entity.parking_slot import ParkingSlot
from enums.slot_size import SlotSize
from messages.messages import SuccessMessages


class ParkingSlotManager:
    def __init__(self):
        self.parking_slot_dao = ParkingSlotDao()
        self.cache = Cache.get_instance()

    def create(self, count, size=SlotSize.MEDIUM.value):
        parking_slots = []
        for i in range(count):
            parking_slots.append(ParkingSlot(size))
        parking_slots = self.parking_slot_dao.bulk_create(parking_slots)
        if not parking_slots:
            return
        for parking_slot in parking_slots:
            self.cache.add_slot(parking_slot.id)
        print(SuccessMessages.PARKING_LOT_CREATION_SUCCESS % count)
        return parking_slots

    def get_all(self):
        return self.parking_slot_dao.get_all()

