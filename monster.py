class Monster:
    def __init__(self, monster_type, health, damage):
        self.type = monster_type
        self.health = health
        self.damage = damage

    def attack(self, target):
        print(f"{self.type} attacks {target.name} for {self.damage} damage!")
        target.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.type} takes {amount} damage. Current health: {self.health}")

    def __str__(self):
        return f"Monster: {self.type}, Health: {self.health}, Damage: {self.damage}"