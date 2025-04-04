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
        
        if self.effect == "damage":
            result["message"] = f"{self.name} deals {self.damage} damage to {target}"
        elif self.effect == "heal":
            result["message"] = f"{self.name} heals {self.damage} health for {target}"
        elif self.effect == "buff":
            result["message"] = f"{self.name} buffs {target}"
        elif self.effect == "debuff":
            result["message"] = f"{self.name} weakens {target}"
        
        return result
    
    def __str__(self):
        return f"{self.name} ({self.effect}, Damage: {self.damage}, Cost: {self.cost})"


