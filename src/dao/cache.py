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
        self._available_slots.remove(slot_id)

    def add_slot(self, slot_id):
        insert_index = 0
        while insert_index < len(self._available_slots) and self._available_slots[insert_index] < slot_id:
            insert_index += 1
        self._available_slots.insert(insert_index, slot_id)

    def get_nearest_slot(self):
        if len(self._available_slots) > 0:
            return self._available_slots[0]
        return None
