class VehicleParkingSlot:
    def __init__(self, parking_slot_id, vehicle_registration_number, enabled=True, _id=None):
        self.id = _id
        self.parking_slot_id = parking_slot_id
        self.vehicle_registration_number = vehicle_registration_number
        self.enabled = enabled
