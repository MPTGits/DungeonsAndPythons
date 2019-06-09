from Charecters.hero import Hero
from Charecters.enemy import Enemy
from .weapon import Weapon
from Dungeon.dungeon import *

class Fight:
    def __init__(self, hero, enemy,dungeon):
        self.hero = hero
        self.enemy = enemy
        self.dungeon = dungeon
    

    @staticmethod
    def greater(a, b):
        if a > b:
            return a
        else:
            return b

    def attack_by_hero(self):
        check_weapon = self.dungeon.hero_can_attack_by_weapon(self.enemy)
        if self.hero.can_attack_by_spell() is True and self.hero.can_attack_by_weapon() is True and check_weapon is True:
            #chosen_attack_damage = self.greater(self.hero.attack(by="weapon"), self.hero.attack(by="spell"))
            chosen_attack_damage = self.greater(self.hero.weapon.get_damage(), self.hero.spell.get_damage())
        elif self.hero.can_attack_by_weapon() is True and check_weapon is True:
            chosen_attack_damage = self.hero.weapon.get_damage()
        elif self.hero.can_attack_by_spell() is True:
            chosen_attack_damage = self.hero.spell.get_damage()
        else:
            chosen_attack_damage = 0
        if chosen_attack_damage == 0:
            print("Hero can't attack, he has no spell and weapon or is out of mana.")
        elif chosen_attack_damage == self.hero.spell.get_damage() and self.hero.can_attack_by_spell():
            self.hero.use_mana(self.hero.spell.get_mana_cost())
            self.enemy.take_damage(chosen_attack_damage)
            print("Hero casts a " + self.hero.spell.get_name() + " ,hits enemy for " + str(chosen_attack_damage) + " dmg.")
            print("Enemy health is " + str(self.enemy.get_health()))
        #Added this so we don't attack with a weapon from miles away
        elif not self.dungeon.hero_attack('weapon'):
            print('Hero cannot cast a spell and is too far to attack by weapon!')
            return
        else:
            self.enemy.take_damage(chosen_attack_damage)
            print("Hero hits enemy with a " + self.hero.weapon.get_name() + " for " + str(chosen_attack_damage) + " dmg.")
            print("Enemy health is " + str(self.enemy.get_health()))

    def attack_by_enemy(self):
        self.hero.take_damage(self.enemy.get_damage())
        print("Enemy hits hero for " + str(self.enemy.get_damage()) + " dmg.")
        print("Hero health is " + str(self.hero.get_health()))




