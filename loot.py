
# Loot class
class Loot:
    def __init__(self, gold=100, weapon=None, potion=None):
        self.gold = gold
        self.weapon = weapon
        self.potion = potion

    def __str__(self):
        return f"Loot(gold={self.gold}, weapon={self.weapon}, potion={self.potion})"