from weapon import Weapon
from spell import Spell

class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.max_health = health
        self.max_mana = mana
        self.weapon = Weapon("",0)
        self.spell = Spell("", 0, 0, 0)

    def known_as(self):
        return self.name + " the " + self.title

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.health != 0

    def can_cast(self):
        return self.mana != 0

    def use_mana(self, mana_points):
        if self.mana >= mana_points:
            self.mana = self.mana - mana_points 
            return True
        return False
    # def helper(self, current, modifier, max):
    #     new = current + modifier

    def take_damage(self, damage_points):
        new_health = self.health - damage_points
        self.health = new_health if new_health > 0 else 0

    def take_healing(self, healing_points):
        if self.is_alive() is True:
            new_health = self.health + healing_points
            self.health = new_health if new_health < self.max_health else self.max_health
            return True
        return False

    def take_mana(self, mana_points=0):
        if mana_points == 0:
            new_mana = self.mana + self.mana_regeneration_rate
            self.mana = new_mana if new_mana < self.max_mana else self.max_mana
        else:
            new_mana = self.mana + mana_points
            self.mana = new_mana if new_mana < self.max_mana else self.max_mana

    def equip(self, weapon):
        self.weapon = weapon

    def can_attack_by_spell(self):
        if self.spell.get_mana_cost() <= self.get_mana() and self.spell.get_mana_cost() != 0:
            return True
        return False

    def can_attack_by_weapon(self):
        return self.weapon.get_damage() > 0

    def learn(self, spell):
        self.spell = spell

    def attack(self, by = ""):
        if by == "weapon":
            return self.weapon.get_damage()
        if by == "spell" and self.spell.get_mana_cost() <= self.mana:
            self.mana-=self.spell.get_mana_cost()
            return self.spell.get_damage()

    
# def chosen_attack(self):


#h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
#w = Weapon(name="The Axe of Destiny", damage=20)
#h.equip(w)
#print(h.weapon)
#s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
#h.learn(s)
#print(h.spell.get_damage())




