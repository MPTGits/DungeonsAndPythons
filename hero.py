class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self._name = name
        self._title = title
        self._health = health
        self._mana = mana
        self._mana_regeneration_rate = mana_regeneration_rate
        self._max_health = health
        self._max_mana = mana
        #self._weapon = Weapon("",0)
        # self._spell = Spell("", 0, 0, 0)

    def known_as(self):
        return self._name + " the " + self._title

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def is_alive(self):
        return self._health != 0

    def can_cast(self):
        return self._mana != 0

    def use_mana(self, mana_points):
        if self._mana >= mana_points:
            self._mana = self._mana - mana_points 
            return True
        return False
    # def helper(self, current, modifier, max):
    #     new = current + modifier

    def take_damage(self, damage_points):
        new_health = self._health - damage_points
        self._health = new_health if new_health > 0 else 0

    def take_healing(self, healing_points):
        if self.is_alive() is True:
            new_health = self._health + healing_points
            self._health = new_health if new_health < self._max_health else self._max_health
            return True
        return False

    def take_mana(self, mana_points=0):
        if mana_points == 0:
            new_mana = self._mana + self._mana_regeneration_rate
            self._mana = new_mana if new_mana < self._max_mana else self._max_mana
        else:
            new_mana = self._mana + mana_points
            self._mana = new_mana if new_mana < self._max_mana else self._max_mana

    def equip(self, weapon):
        self._weapon = weapon

    def can_attack_by_spell(self):
        if self._spell.get_mana_cost() <= self.get_mana() and self._spell.get_mana() != 0:
            return True
        return False

    def can_attack_by_weapon(self):
        return self._weapon.get_damage() > 0


class Weapon:
    def __init__(self, name, damage):
        self._name = name
        self._damage = damage

    def __eq__(self, other):
        return self._name == other._name and self._damage == other._damage

    def get_damage(self):
        return self._damage

    def __str__(self):
        return 'You have found '+self._name+' with '+str(self._damage)+' damage'

    def get_name(self):
        return self._name

    def get_damage(self):
        return self._damage
    # def learn(self, spell):
    #     self.spell = spell

    # def attack(self, by = ""):
    #     if by == "weapon":
    #         return self.weapon.get_damage()
    #     if by == "spell" and self._spell.get_mana_cost() <= self._mana
    #         return self._spell.get_damage()
# def chosen_attack(self):