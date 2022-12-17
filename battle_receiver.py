
import sys

#RECEIVER
#====================================
class BattleReceiver():

    @staticmethod
    def run_command_DisplayPlayers(object):
        new_map = map(lambda x: x.display, object)
        for lines in zip(*new_map):
            print(*lines)


    @staticmethod
    def run_command_DisplayOptions(object):
        string = (
        '                                        \n'
        '  |     {0:11}     |     {1:11}     |   \n'
        '  |     {2:11}     |     {3:11}     |   \n'
        '                                        \n'
        '                                        \n'
        ).format(
             format(object[0], ' <2')
            ,format(object[1], ' <2')
            ,format(object[2], ' <2')
            ,format(object[3], ' <2')
        )
        print(string)


    @staticmethod
    def run_command_DisplayAbilities(object):
        pass