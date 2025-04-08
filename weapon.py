from attack import Attack

class Weapon:
    def __init__(self, name, damage, effect=None):
        self.name = name
        self.damage = damage
        self.attack = Attack(name, damage, effect) 

    def __str__(self):
        return f"{self.name} (Damage: {self.damage})"
