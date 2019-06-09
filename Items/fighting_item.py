class FightingItem:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

        
    def __eq__(self, other):
        return self.get_name() == other.get_name() and self.get_damage() == other.get_damage()

    def get_damage(self):
        return self.damage

    def __str__(self):
        return 'You have found ' + self.get_name() + ' with ' + str(self.get_damage()) + ' damage'

    def get_name(self):
        return self.name