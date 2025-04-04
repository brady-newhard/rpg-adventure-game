class inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
        else:
            print(f"Cannot remove {quantity} of {item_name}. Not enough stock or item does not exist.")

    def check_stock(self, item_name):
        return self.items.get(item_name, 0)

    def list_items(self):
        return self.items
    def __str__(self):
        return f"Inventory: {self.items}"