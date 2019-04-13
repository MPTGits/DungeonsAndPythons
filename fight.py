from dungeon import *

class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    @staticmethod
    def greater(a, b):
        if a > b:
            return a
        else:
            return b

    def attack_by_hero(self):
        if self.hero.can_attack_by_spell() is True:
            chosen_attack_damage = greater(self.hero.attack(by="weapon"), self.hero.attack(by="spell")) 
        elif self.hero.can_attack_by_weapon() is True:
            chosen_attack_damage = self.hero.weapon.get_damage()
        else:
            chosen_attack_damage = 0
        if chosen_attack_damage == 0:
            print("Hero can't attack, he has no spell and weapon.")
        elif chosen_attack_damage == self.hero.spell.get_damage() and self.hero.can_attack_by_spell():
            self.hero.use_mana(self.hero.spell.get_mana_cost())
            enemy.take_damage(chosen_attack_damage)
            print("Hero casts a " + self.hero.spell.get_name() + " ,hits enemy for " + str(chosen_attack_damage) + " dmg.")
            print("Enemy health is " + str(self.enemy.get_health()))
        else:
            enemy.take_damage(chosen_attack_damage)
            print("Hero hits enemy with a " + self.hero.weapon.get_name() + " for " + str(chosen_attack_damage) + " dmg.")
            print("Enemy health is " + str(self.enemy.get_health()))

    def attack_by_enemy(self):
        self.hero.take_damage(self.enemy.get_damage())
        print("Enemy hits hero for " + str(self.enemy.get_damage()) + " dmg.")
        print("Hero health is " + str(self.hero.get_health()))


# enemy = Enemy(health=100, mana=100, damage=20)
# h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
# w = Weapon(name="The Axe of Destiny", damage=20)
# h.equip(w)
# fight = Fight(h, enemy)
# fight.attack_by_hero()
# fight.attack_by_enemy()