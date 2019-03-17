from manager.command_manager import CommandManager


class Executor:
    def __init__(self):
        self.command_manager = CommandManager()

    def execute(self, file_path=None):
        if file_path:
            pass
        else:
            while True:
                try:
                    input_string = input()
                    input_list = input_string.split()
                    command = input_list[0]
                    args = input_list[1:]
                    self.command_manager.manage(command, args)
                except Exception as e:
                    print(e)
