class weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        

    def __str__(self):
        return f"Weapon: {self.name}, Damage: {self.damage}"
