from interface_command import ICommand

class CommandAttack(ICommand):

    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def execute(self):
        damage = self.attacker.attack - self.defender.defense
        if damage > 0:
            self.defender.take_damage(damage)
        else:
            damage = 0
        print(f"{self.attacker.name} attacks {self.defender.name} for {damage} damage!")