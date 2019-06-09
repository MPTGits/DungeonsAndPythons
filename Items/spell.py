from .fighting_item import FightingItem

class Spell(FightingItem):

    def __init__(self,name,damage,mana_cost,cast_range):
        super().__init__(name,damage)
        self.mana_cost=mana_cost
        self.cast_range=cast_range

    def get_mana_cost(self):
        return self.mana_cost
    
    def get_cast_range(self):
        return self.cast_range
