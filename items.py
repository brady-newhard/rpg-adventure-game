class Item:
    def __init__(self, name, item_type, effect=None):
        self.name = name
        self.item_type = item_type
        self.effect = effect

    def __str__(self):
        return f"{self.name} ({self.item_type}, Effect: {self.effect})"