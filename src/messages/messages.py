class SuccessMessages:
    PARKING_LOT_CREATION_SUCCESS = 'Created a parking lot with %d slots'
    PARKING_VEHICLE_SUCCESS = 'Allocated slot number: %d'
    LEAVE_PARKING_SLOT_SUCCESS = 'Slot number %d is free'
    STATUS_HEADER = 'Slot No.\tRegistration No\tColour'
    NO_VEHICLE_PARKED_AT_PARKING_SLOT = 'No vehicle parked at the parking slot'


class ErrorMessages:
    INVALID_ARGUMENTS = 'Invalid arguments'
    INVALID_COMMAND = 'Invalid command'
    INVALID_COMMAND_OR_ARGUMENTS = 'Invalid arguments or command'
    FILE_NOT_FOUND = 'File not found'
    NOT_FOUND = 'Not found'
    ERROR_WHILE_READING_FILE = 'Error while reading input from file'
    ERROR_WHILE_CONSOLE_INPUT = 'Error while reading input from console'
    PARKING_LOT_NOT_INITIALIZED = 'Parking lot not initialized'
    PARKING_FULL = 'Sorry, parking lot is full'
    PARKING_LOT_DOES_NOT_EXISTS = 'Parking lot does not exists, Please create a new parking lot'
    VEHICLE_WITH_REGISTRATION_DOES_NOT_EXISTS = 'Vehicle with registration number does not exists'
