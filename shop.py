class Shop:
    def __init__(self, potions, spells):
        self.potions = potions
        self.spells = spells

    def __str__(self):
        return "Shop"
    
    def buy(self, item):
        return item
    
    def sell(self, item):
        return item
