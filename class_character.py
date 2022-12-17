class Character:

    def __init__(self, num, name):
        self.num = num          # Player number with base 1
        self.pos = self.num - 1      # Player number with base 0 (for lists)
        self.name = name
        self.is_downed = False
        self.display = self.MakeDisplay()


    def MakeDisplay(self):
        string = (
        '              \n'
        '  ==========  \n'
        '  │ PLAYER │  \n'
        '  │   {}   │  \n'
        '  ==========  \n'
        '              \n'
        ).format(
            format(self.num, ' <2')
        ).splitlines()
        return string    


class Fighter(Character):
    def __init__(self, num, name):
        super().__init__(num, name) 
        self.hp_max = 500
        self.hp_current = self.hp_max
        self.strength = 8
        self.defense = 5
        self.speed = 8
        self.luck = 2
        self.options = ["Light Attack", "Heavy Attack", "Defend", "Meditate"]
        self.abilities = []


class WhiteMage(Character):
    def __init__(self, num, name):
        super().__init__(num, name) 
        self.hp_max = 250
        self.hp_current = self.hp_max
        self.strength = 3
        self.defense = 5
        self.speed = 3
        self.luck = 8
        self.options = ["Light Attack", "White Magic", "Defend", "Meditate"]
        self.abilities = []

class DarkMage(Character):
    def __init__(self, num, name):
        super().__init__(num, name) 
        self.hp_max = 250
        self.hp_current = self.hp_max
        self.strength = 5
        self.defense = 5
        self.speed = 3
        self.luck = 6
        self.options = ["Light Attack", "Dark Magic", "Defend", "Meditate"]
        self.abilities = []

class Witch(Character):
    def __init__(self, num, name):
        super().__init__(num, name)  
        self.hp_max = 250
        self.hp_current = self.hp_max
        self.strength = 3
        self.defense = 3
        self.speed = 3
        self.luck = 3
        self.options = ["White Magic", "Dark Magic", "Defend", "Meditate"]
        self.abilities = []

class Bruiser(Character):
    def __init__(self, num, name):
        super().__init__(num, name) 
        self.hp_max = 250
        self.hp_current = self.hp_max
        self.strength = 7
        self.defense = 2
        self.speed = 3
        self.luck = 3
        self.options = ['Unarmed', 'Special', 'Defend', 'Meditate']
        self.abilities = []

class Druid(Character):
    def __init__(self, num, name):
        super().__init__(num, name) 
        self.hp_max = 250
        self.hp_current = self.hp_max
        self.strength = 3
        self.defense = 3
        self.speed = 3
        self.luck = 3
        self.options = ["Light Attack", "ShapeShift", "Defend", "Meditate"]
        self.abilities = []

class DruidFIRE(Character):
    def __init__(self, num, name):
        super().__init__(num, name) 
        self.hp_max = 250
        self.hp_current = self.hp_max
        self.strength = 3
        self.defense = 3
        self.speed = 3
        self.luck = 3
        self.options = ["Light Attack", "Heavy Attack", "Defend", "Meditate"]
        self.abilities = []

class DruidWATER(Character):
    def __init__(self, num, name):
        super().__init__(num, name) 
        self.hp_max = 250
        self.hp_current = self.hp_max
        self.strength = 3
        self.defense = 3
        self.speed = 3
        self.luck = 3
        self.options = ["Light Attack", "Heavy Attack", "Defend", "Meditate"]
        self.abilities = []

class DruidEARTH(Character):
    def __init__(self, num, name):
        super().__init__(num, name) 
        self.hp_max = 250
        self.hp_current = self.hp_max
        self.strength = 3
        self.defense = 3
        self.speed = 3
        self.luck = 3
        self.options = ["Light Attack", "Heavy Attack", "Defend", "Meditate"]
        self.abilities = []

class DruidWIND(Character):
    def __init__(self, num, name):
        super().__init__(num, name) 
        self.hp_max = 250
        self.hp_current = self.hp_max
        self.strength = 3
        self.defense = 3
        self.speed = 3
        self.luck = 3
        self.options = ["Light Attack", "Heavy Attack", "Defend", "Meditate"]
        self.abilities = []

class Dragon(Character):
    def __init__(self, num, name):
        super().__init__(num, name)  
        self.hp_max = 5000
        self.hp_current = self.hp_max
        self.strength = 10
        self.defense = 10
        self.speed = 10
        self.luck = 10
        self.options = ["Attack", "Magic", "Special", "Mediate"]
        self.abilities = []

class Empty(Character):
    def __init__(self, num, name):
        super().__init__(num, name) 
        self.hp_max = 0
        self.hp_current = self.hp_max
        self.strength = 0
        self.defense = 0
        self.speed = 0
        self.luck = 0
        self.options = []
        self.abilities = []