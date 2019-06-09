from .fighting_item import FightingItem

class Weapon(FightingItem):
    def __init__(self, name, damage):
        super().__init__(name,damage)