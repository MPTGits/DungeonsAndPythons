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

    def attack_by_hero():
        pass

    def attack_by_enemy():
        pass

# wrong
    def start(self):
        while(self.hero.is_alive() and self.enemy.is_alive()):
            if self.hero.can_attack_by_spell() is True:
                chosen_attack_damage = greater(self.hero.attack(by="weapon"), self.hero.attack(by="spell")) 
            elif self.hero.can_attack_by_weapon() is True:
                chosen_attack_damage = self.hero.spell.get_damage()
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
                print("Hero hits with a " + self.hero.weapon.get_name() + " enemy for " + str(chosen_attack_damage) + " dmg.")
                print("Enemy health is " + str(self.enemy.get_health()))
            if enemy is at heros position:
                then he attacks hero 
            else:
                moves 1 step closer to hero