from enums.command import Command
from manager.parking_slot_manager import ParkingSlotManager
from manager.vehicle_manager import VehicleManager
from manager.vehicle_parking_slot_manager import VehicleParkingSlotManager
from messages.messages import ErrorMessages, SuccessMessages


class CommandManager:
    def __init__(self):
        self.parking_slot_manager = ParkingSlotManager()
        self.vehicle_manager = VehicleManager()
        self.vehicle_parking_slot_manager = VehicleParkingSlotManager()

    def manage(self, command, args):
        command = command.strip().upper()
        if command == Command.CREATE_PARKING_LOT.name:
            if len(args) != Command.CREATE_PARKING_LOT.value[1]:
                print('Invalid arguments.')
            number_of_slots = int(args[0])
            self.parking_slot_manager.create(number_of_slots)
        elif command == Command.PARK.name:
            if len(args) != Command.PARK.value[1]:
                print('Invalid arguments.')
            registration_number = args[0]
            color = args[1]
            if self.vehicle_parking_slot_manager.park(registration_number):
                self.vehicle_manager.create(registration_number, color)
        elif command == Command.LEAVE.name:
            if len(args) != Command.LEAVE.value[1]:
                print('Invalid arguments.')
            slot_number = int(args[0])
            self.vehicle_parking_slot_manager.leave(slot_number)
        elif command == Command.STATUS.name:
            if len(args) != Command.STATUS.value[1]:
                print('Invalid arguments.')
            self.vehicle_parking_slot_manager.get_status()
        elif command == Command.REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR.name:
            if len(args) != Command.REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR.value[1]:
                print('Invalid arguments.')
            color = args[0]
            self.vehicle_manager.get_vehicles_by_color(color, printing=True)
        elif command == Command.SLOT_NUMBERS_FOR_CARS_WITH_COLOUR.name:
            if len(args) != Command.SLOT_NUMBERS_FOR_CARS_WITH_COLOUR.value[1]:
                print('Invalid arguments.')
            color = args[0]
            self.vehicle_parking_slot_manager.get_slot_numbers_for_color(color)
        elif command == Command.SLOT_NUMBER_FOR_REGISTRATION_NUMBER.name:
            if len(args) != Command.SLOT_NUMBER_FOR_REGISTRATION_NUMBER.value[1]:
                print('Invalid arguments.')
            registration_number = args[0]
            self.vehicle_parking_slot_manager.get_by_registration_number(registration_number)
        else:
            raise Exception(ErrorMessages.INVALID_COMMAND)
