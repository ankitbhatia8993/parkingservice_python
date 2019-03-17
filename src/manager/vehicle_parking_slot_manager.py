from dao.inmemory import VehicleParkingSlotDao
from entity.vehicle_parking_slot import VehicleParkingSlot


class VehicleParkingSlotManager:
    def __init__(self):
        self.vehicle_parking_slot_dao = VehicleParkingSlotDao()

    def park(self, registration_number, parking_slot_id):
        vehicle_parking_slot = VehicleParkingSlot(parking_slot_id, registration_number)
        return self.vehicle_parking_slot_dao.create(vehicle_parking_slot)

