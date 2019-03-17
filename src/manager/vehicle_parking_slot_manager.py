from dao.cache import Cache
from dao.inmemory import VehicleParkingSlotDao
from entity.vehicle_parking_slot import VehicleParkingSlot
from manager.vehicle_manager import VehicleManager


class VehicleParkingSlotManager:
    def __init__(self):
        self.vehicle_parking_slot_dao = VehicleParkingSlotDao()
        self.vehicle_manager = VehicleManager()
        self.cache = Cache.get_instance()

    def park(self, registration_number):
        parking_slot_id = self.cache.get_nearest_slot()
        if parking_slot_id:
            vehicle_parking_slot = VehicleParkingSlot(parking_slot_id, registration_number)
            vehicle_parking_slot = self.vehicle_parking_slot_dao.create(vehicle_parking_slot)
            self.cache.remove_slot(parking_slot_id)
            print('Allocated slot number: %d' % vehicle_parking_slot.parking_slot_id)
            return vehicle_parking_slot
        else:
            print('Sorry, parking lot is full')
            return None

    def leave(self, slot_number):
        self.vehicle_parking_slot_dao.disable_vehicle_parking(slot_number)
        self.cache.add_slot(slot_number)
        print('Slot number %d is free' % slot_number)

    def get_status(self):
        vehicle_parking_slots = self.vehicle_parking_slot_dao.get_all()
        print('Slot No.\tRegistration No\tColour')
        for vehicle_parking_slot in vehicle_parking_slots:
            registration_number = vehicle_parking_slot.vehicle_registration_number
            vehicle = self.vehicle_manager.get(registration_number)
            print('%d\t%s\t%s' % (vehicle_parking_slot.parking_slot_id, registration_number, vehicle.color))

    def get_slot_numbers_for_color(self, color):
        vehicles = self.vehicle_manager.get_vehicles_by_color(color)
        slot_numbers = []
        for vehicle in vehicles:
            vehicle_parking_slot = self.vehicle_parking_slot_dao.get_by_vehicle(vehicle.registration_number)
            if vehicle_parking_slot:
                slot_numbers.append(vehicle_parking_slot.parking_slot_id)
        print(', '.join(map(lambda s: str(s), slot_numbers)))
        return slot_numbers

    def get_by_registration_number(self, registration_number):
        vehicle_parking_slot = self.vehicle_parking_slot_dao.get_by_vehicle(registration_number)
        if vehicle_parking_slot:
            print(vehicle_parking_slot.parking_slot_id)
        else:
            print('Not found')
        return vehicle_parking_slot


