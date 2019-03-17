from sys import argv
from application import Executor


if __name__ == '__main__':
    arguments = argv
    executor = Executor()

    if len(arguments) > 1:
        file_path = arguments[0]
        executor.execute(file_path)
    else:
        executor.execute()



