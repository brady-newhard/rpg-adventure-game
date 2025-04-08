from characters import PlayerCharacter
from weapon import Weapon
from monster import Monster
from loot import Loot
from potion import Potion
from quest import Quest
from gameEngine import GameEngine

starter_weapon = Weapon("Iron Sword", 10)
goblin_weapon = Weapon("Goblin Dagger", 5)

player = PlayerCharacter("Aria", starter_weapon)
monster_loot = Loot(gold=50, weapon=goblin_weapon, potion=Potion("Health", 10, 15))
goblin = Monster("Goblin", 30, goblin_weapon, monster_loot)

quest1 = Quest("Goblin Menace", "A goblin has been terrorizing the village. Defeat it!", goblin)
engine = GameEngine(player)
engine.start_quest(quest1)
