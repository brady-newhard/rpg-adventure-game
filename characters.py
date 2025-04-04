# Each class must have:
# An __init__ method
# At least one instance method (e.g., attack(), heal(), etc.)
# A __str__() or __repr__() for easy printing
# Use instance attributes to track state (like health, gold, inventory).
# Interact via method calls (player.attack(monster)).
class Player_characters():
    def __init__( self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack (self, target):
        target.health -= self.attack
        print(f"{self.name} attacks {target.name} for {self.attack} damage!")
        print(f"{target.name}'s health is now {target.health}")
    
        if target.health <= 0:
            print(f"{target.name} has been defeated!")
            return True
        return False
    def __str__(self):
        return f"Player: {self.name}, Health: {self.health}, Attack: {self.attack}"
    