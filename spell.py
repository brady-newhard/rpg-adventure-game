class Spell:
    def __init__(self, name, damage, effect, cost):
        self.name = name
        self.damage = damage
        self.effect = effect
        self.cost = cost
    
    def cast(self, target):
        result = {
            "spell_name": self.name,
            "effect": self.effect,
            "damage": self.damage,
            "cost": self.cost
        }
        



