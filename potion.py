class Potion:
    def __init__(self, type, effect, cost):
        self.type = type
        self.effect = effect
        self.cost = cost
    
    def heal(self):
        return self.effect
    
    def buff(self):
        return self.effect

    def __str__(self):
        return f"{self.type} potion (Effect: {self.effect}, Cost: {self.cost} gold)"
