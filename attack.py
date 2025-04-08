class Attack:
    def __init__(self, name, damage, effect=None):
        self.name = name
        self.damage = damage
        self.effect = effect 

    def execute(self, attacker, target):
        print(f"{attacker.name} uses {self.name}!")
        
        target.take_damage(self.damage)

        if self.effect:
            print(f"The attack causes a {self.effect} effect!")

    def __str__(self):
        return f"{self.name} (Damage: {self.damage}, Effect: {self.effect})"
