class Cache:
    __instance = None
    _available_slots = []

    def __init__(self):
        if Cache.__instance:
            raise Exception("This class is a singleton!")
        else:
            Cache.__instance = self

    @staticmethod
    def get_instance():
        if not Cache.__instance:
            Cache()
        return Cache.__instance

    def remove_slot(self, slot_id):
        if not isinstance(self._available_slots, list):
            self.load()
            return
        self._available_slots.remove(slot_id)

    def add_slot(self, slot_id):
        if not isinstance(self._available_slots, list):
            self.load()
            return
        insert_index = 0
        while insert_index < len(self._available_slots) and self._available_slots[insert_index] < slot_id:
            insert_index += 1
        self._available_slots.insert(insert_index, slot_id)

    def get_nearest_slot(self):
        if not isinstance(self._available_slots, list):
            self.load()
        if len(self._available_slots) > 0:
            return self._available_slots[0]
        return None

    def load(self):
        from manager.vehicle_parking_slot_manager import VehicleParkingSlotManager
        vehicle_parking_slot = VehicleParkingSlotManager()
        available_slots = vehicle_parking_slot.get_available_slots()
        self._available_slots = sorted(available_slots)
