from loot import Loot

class Monster:
    def __init__(self, name, health, weapon, loot: Loot):
        self.name = name
        self.health = health
        self.weapon = weapon  # this should be a Weapon object
        self.loot = loot

    def attack(self, target):
        print(f"{self.name} attacks {target.name} with {self.weapon.name}!")
        self.weapon.attack.execute(self, target)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Current health: {self.health}")

    def drop_loot(self):
        return self.loot

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Monster: {self.name}, Health: {self.health}, Weapon: {self.weapon.name}"
