from enum import Enum

from enums.slot_size import SlotSize


class VehicleType(Enum):
    BIKE = SlotSize.SMALL
    CAR = SlotSize.MEDIUM
    TRUCK = SlotSize.LARGE
    BUS = SlotSize.LARGE
