class Quest:
    def __init__(self, title, description, monster):
        self.title = title
        self.description = description
        self.monster = monster

    def __str__(self):
        return f"Quest: {self.title.title()}\n{self.description}\n"