from enums.command import Command
from manager.parking_slot_manager import ParkingSlotManager
from manager.vehicle_manager import VehicleManager
from manager.vehicle_parking_slot_manager import VehicleParkingSlotManager


class CommandManager:
    def __init__(self):
        self.parking_slot_manager = ParkingSlotManager()
        self.vehicle_manager = VehicleManager()
        self.vehicle_parking_slot_manager = VehicleParkingSlotManager()

    def manage(self, command, args):
        command = command.upper()
        if command == Command.CREATE_PARKING_LOT.name:
            if len(args) != Command.CREATE_PARKING_LOT.value:
                print('Invalid arguments.')
            number_of_slots = args[0]
            self.parking_slot_manager.create(number_of_slots)
        elif command == Command.PARK.name:
            if len(args) != Command.PARK.value:
                print('Invalid arguments.')
            registration_number = args[0]
            color = args[1]
            self.vehicle_manager.create(registration_number, color)
            self.parking_slot_manager.parking_slot_dao
        elif command == Command.LEAVE.name:
            if len(args) != Command.LEAVE.value:
                print('Invalid arguments.')
        elif command == Command.STATUS.name:
            if len(args) != Command.STATUS.value:
                print('Invalid arguments.')
        elif command == Command.REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR.name:
            if len(args) != Command.REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR.value:
                print('Invalid arguments.')
        elif command == Command.SLOT_NUMBERS_FOR_CARS_WITH_COLOUR:
            if len(args) != Command.SLOT_NUMBERS_FOR_CARS_WITH_COLOUR.value:
                print('Invalid arguments.')
        elif command == Command.SLOT_NUMBER_FOR_REGISTRATION_NUMBER:
            if len(args) != Command.SLOT_NUMBER_FOR_REGISTRATION_NUMBER.value:
                print('Invalid arguments.')
        else:
            print('Invalid command.')
