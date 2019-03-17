from _datetime import datetime
from collections import defaultdict

parking_slot_data = {
    'id_counter': 1,
    'id_to_object': defaultdict()
}

vehicle_data = {
    'id_to_object': defaultdict()
}

vehicle_parking_slot_data = {
    'id_counter': 1,
    'id_to_object': defaultdict()
}


class ParkingSlotDao:
    """
    id, size, status
    """
    def bulk_create(self, parking_slots):
        existing_size = len(parking_slot_data['id_to_object'])
        if existing_size > 0:
            raise Exception('Parking lot is already created with size %d' % existing_size)
        created_parking_slots = []
        for parking_slot in parking_slots:
            _id = parking_slot_data['id_counter']
            parking_slot.id = _id
            parking_slot_data['id_to_object'][_id] = parking_slot
            parking_slot_data['id_counter'] += 1
            created_parking_slots.append(parking_slot)
        return created_parking_slots

    def update(self, parking_slot):
        _id = parking_slot.id
        parking_slot_data['id_to_object'][_id] = parking_slot
        return parking_slot


class VehicleDao:
    """
    registration_number, color, type, created_on
    """
    def create(self, vehicle):
        registration_number = vehicle.registration_number
        if registration_number in vehicle_data['id_to_object'].keys():
            return vehicle_data['id_to_object'][registration_number]
        vehicle.created_on = datetime.now()
        vehicle_data['id_to_object'][registration_number] = vehicle

    def get(self, registration_number):
        return vehicle_data['id_to_object'].get(registration_number)

    def update(self, vehicle):
        _id = vehicle.id
        vehicle_data['id_to_object'][_id] = vehicle
        return vehicle

    def get_vehicles_by_color(self, color):
        entries = vehicle_data['id_to_object'].values()
        return list(filter(lambda entry: entry.color == color, entries))


class VehicleParkingSlotDao:
    """
    id, parking_slot_id, vehicle_registration_number, enabled, created_on
    """
    def create(self, vehicle_parking_slot):
        parking_slot_id = vehicle_parking_slot.parking_slot_id
        vehicle_registration_number = vehicle_parking_slot.vehicle_registration_number
        vehicle_parking_slot_entries = vehicle_parking_slot_data['id_to_object'].values()
        filtered_entries = list(filter(lambda entry: entry.parking_slot_id == parking_slot_id
                                       and entry.vehicle_registration_number == vehicle_registration_number
                                       and entry.enabled, vehicle_parking_slot_entries))
        if len(filtered_entries) > 0:
            raise 'Vehicle with registration number %s is already parked at parking slot %s' \
                  % (vehicle_registration_number, parking_slot_id)
        _id = vehicle_parking_slot_data['id_counter']
        vehicle_parking_slot.id = _id
        vehicle_parking_slot.created_on = datetime.now()
        vehicle_parking_slot_data['id_to_object'][_id] = vehicle_parking_slot
        vehicle_parking_slot_data['id_counter'] += 1
        return vehicle_parking_slot

    def get_all(self):
        return list(filter(lambda entry: entry.enabled, vehicle_parking_slot_data['id_to_object'].values()))

    def update(self, vehicle_parking_slot):
        _id = vehicle_parking_slot.id
        vehicle_parking_slot_data['id_to_object'][_id] = vehicle_parking_slot

    def get_by_parking_slot(self, parking_slot_id):
        vehicle_parking_slot_entries = vehicle_parking_slot_data['id_to_object'].values()
        filtered_entries = list(filter(lambda entry: entry.parking_slot_id == parking_slot_id and entry.enabled,
                                       vehicle_parking_slot_entries))
        if len(filtered_entries) > 0:
            return filtered_entries[0]
        return None

    def get_by_vehicle(self, vehicle_registration_number):
        vehicle_parking_slot_entries = vehicle_parking_slot_data['id_to_object'].values()
        filtered_entries = list(filter(lambda entry: entry.vehicle_registration_number == vehicle_registration_number
                                       and entry.enabled, vehicle_parking_slot_entries))
        if len(filtered_entries) > 0:
            return filtered_entries[0]
        return None

    def disable_vehicle_parking(self, parking_slot_id):
        vehicle_parking_slot = self.get_by_parking_slot(parking_slot_id)
        _id = vehicle_parking_slot.id
        vehicle_parking_slot_data['id_to_object'][_id].enabled = False

