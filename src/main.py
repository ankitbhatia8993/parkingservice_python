from sys import argv
from application import Executor
from messages.messages import ErrorMessages


if __name__ == '__main__':
    arguments = argv
    executor = Executor()

    if len(arguments) == 2:
        file_path = arguments[1]
        executor.execute(file_path)
    elif len(arguments) == 1:
        executor.execute()
    else:
        print(ErrorMessages.INVALID_COMMAND_OR_ARGUMENTS)



