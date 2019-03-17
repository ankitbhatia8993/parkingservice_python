from enum import Enum


class Command(Enum):
    CREATE_PARKING_LOT = ('create_parking_lot', 1)
    PARK = ('park', 2)
    LEAVE = ('leave', 1)
    STATUS = ('status', 0)
    REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR = ('registration_numbers_for_cars_with_colour', 1)
    SLOT_NUMBERS_FOR_CARS_WITH_COLOUR = ('slot_numbers_for_cars_with_colour', 1)
    SLOT_NUMBER_FOR_REGISTRATION_NUMBER = ('slot_number_for_registration_number', 1)

