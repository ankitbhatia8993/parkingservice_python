from manager.command_manager import CommandManager


class Executor:
    def __init__(self):
        self.command_manager = CommandManager()

    def get_command_and_args(self, input_string):
        input_list = input_string.split()
        if len(input_list) == 0:
            print('No command.')
            return None, None
        command = input_list[0]
        args = []
        if len(input_list) > 1:
            args = input_list[1:]
        return command, args

    def execute(self, file_path=None):
        if file_path:
            text_file = open(file_path, "r")
            lines = text_file.readlines()
            for line in lines:
                command, args = self.get_command_and_args(line)
                if command:
                    self.command_manager.manage(command, args)
        else:
            while True:
                try:
                    line = input()
                    command, args = self.get_command_and_args(line)
                    if command:
                        self.command_manager.manage(command, args)
                except Exception as e:
                    print(e)
