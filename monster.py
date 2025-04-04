from loot import Loot

class Monster:
    def __init__(self, monster_name, health, damage, loot: Loot):
        self.type = monster_name
        self.health = health
        self.damage = damage
        self.loot = loot

    def attack(self, target):
        print(f"{self.type} attacks {target.name} for {self.damage} damage!")
        target.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.type} takes {amount} damage. Current health: {self.health}")
    
    def drop_loot(self):
        return self.loot

    def __str__(self):
        return f"Monster: {self.type}, Health: {self.health}, Damage: {self.damage}"