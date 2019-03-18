class ParkingSlot:
    def __init__(self, slot_size, _id=None):
        self.id = _id
        self.size = slot_size

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
