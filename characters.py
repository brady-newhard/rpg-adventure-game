from inventory import Inventory

class PlayerCharacter:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.gold = 0
        self.weapon = weapon
        self.inventory = Inventory()

    def attack(self, target):
        print(f"{self.name} attacks {target.name} with {self.weapon.name}!")
        self.weapon.attack.execute(self, target)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health is now {self.health}")

    def is_alive(self):
        return self.health > 0

    def collect_loot(self, loot):
        print(f"{self.name} collects loot: {loot}")
        self.gold += loot.gold
        if loot.weapon:
            self.inventory.add(loot.weapon)
        if loot.potion:
            self.inventory.add(loot.potion)

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Gold: {self.gold})"
