from interface_command import ICommand

class CommandDisplayPlayers(ICommand):
    def __init__(self, receiver, obj):
        self._receiver = receiver
        self._obj = obj

    def execute(self, *obj):
        self._receiver.run_command_DisplayPlayers(self._obj)  


class CommandDisplayOptions(ICommand):
    def __init__(self, receiver, obj):
        self._receiver = receiver
        self._obj = obj

    def execute(self, *obj):
        self._receiver.run_command_DisplayOptions(self._obj) 


class CommandDisplayAbilities(ICommand):
    def __init__(self, receiver, obj):
        self._receiver = receiver
        self._obj = obj

    def execute(self, *obj):
        self._receiver.run_command_DisplayAbilities(self._obj) 