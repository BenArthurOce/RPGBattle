from battle_invoker import BattleInvoker
from battle_receiver import BattleReceiver
from class_attack import Attack
from class_battle import Battle
from class_character import *
from command_attack import CommandAttack
from command_display import *


                        #DISPLAY        ACTION          BASE    TIMES   TRGTS   CHANCE
                        #NAME           TYPE            DMG     ATTK    HIT     TO HIT
atk_sword       = Attack("Sword",       "Attacking",     51,     4,      1,     0.80)
atk_axe         = Attack("Axe",         "Attacking",     52,     1,      1,     0.80)
atk_spear       = Attack("Spear",       "Attacking",     53,     7,      1,     0.70)
atk_hammer      = Attack("Hammer",      "Attacking",     54,     3,      1,     0.90)
atk_grtsword    = Attack("Greatsword",  "Attacking",    501,     1,      1,     0.05)
atk_grtaxe      = Attack("GreatAxe",    "Attacking",    502,     1,      1,     0.05)
atk_trident     = Attack("Trident",     "Attacking",    504,     1,      1,     0.05)
atk_mrnstar     = Attack("MorningStar", "Attacking",    503,     1,      1,     0.05)
atk_ice         = Attack("Ice",         "Attacking",    201,     1,      1,     0.50)
atk_drain       = Attack("Drain",       "Attacking",    101,     1,      1,     0.90)
atk_bees        = Attack("Bees",        "Attacking",     63,    15,      1,     0.50)
atk_bow         = Attack("Bow",         "Attacking",    100,     1,      1,     1.00)
atk_fireBreath  = Attack("Fire Breath", "Attacking",    120,     1,      1,     1.00)
atk_tailSlam    = Attack("Tail Slam",   "Attacking",     65,     1,      1,     1.00)
atk_bite        = Attack("Bite",        "Attacking",     70,     1,      1,     1.00)
atk_scratch     = Attack("Scratch",     "Attacking",     75,     1,      1,     1.00)
atk_thunder     = Attack("Thunder",     "Attacking",    200,     1,      2,     1.00)
atk_fire        = Attack("Fire",        "Attacking",    250,     1,      2,     1.00)
atk_earthquake  = Attack("EarthQuake",  "Attacking",    300,     1,      2,     1.00)
atk_nothing     = Attack("-",           "Attacking",    300,     1,      2,     1.00)

Player1 = Fighter(1, "Player1")
Player2 = Druid(2, "Player2")
Player3 = DarkMage(3, "Player3")
playerList=[Player1, Player2, Player3]
#Enemy = Character("Dragon", 100, 20, 10)
Enemy = Dragon(1,"Dragon")

GameBattle = Battle(playerList=[Player1, Player2, Player3], enemyList=[Enemy])

print(Player1.defense)
print(Player1.is_downed)
print(Enemy.hp_current)


# Create a receiver
Receiver = BattleReceiver()
DISPLAY_PLAYERS = CommandDisplayPlayers(Receiver, GameBattle.playerList)
DISPLAY_OPTIONS_1 = CommandDisplayOptions(Receiver, Player1.options)
DISPLAY_OPTIONS_2 = CommandDisplayOptions(Receiver, Player2.options)
DISPLAY_OPTIONS_3 = CommandDisplayOptions(Receiver, Player3.options)

Invoker = BattleInvoker()
Invoker.register("DisplayPlayers",DISPLAY_PLAYERS)
Invoker.register("DisplayOptions1",DISPLAY_OPTIONS_1)
Invoker.register("DisplayOptions2",DISPLAY_OPTIONS_2)
Invoker.register("DisplayOptions3",DISPLAY_OPTIONS_3)

Invoker.execute("DisplayPlayers")
Invoker.execute("DisplayOptions1")
Invoker.execute("DisplayOptions2")
Invoker.execute("DisplayOptions3")