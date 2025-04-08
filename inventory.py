class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        print(f"Added {item} to inventory.")
        self.items.append(item)

    def show(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Inventory contains:")
            for item in self.items:
                print(f" - {item}")
