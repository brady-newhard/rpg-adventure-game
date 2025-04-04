from quest import Quest
from battle import battle

class GameEngine:
    def __init__(self, player):
        self.player = player

    def start_quest(self, quest):
        print(f"\n Starting Quest: {quest.title.title()}")
        print(quest)
        battle(self.player, quest.monster)