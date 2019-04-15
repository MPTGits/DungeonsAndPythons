from hero import Weapon
from random import choice,randint,random
from spell import Spell

class Treasure:

    def __init__(self):
        self.found_loot=None
        self.generate_tresures()

    def generate_tresures(self):
        damage=int(randint(1,70)/(random()+1))
        type_wepon_or_spell=choice(("Axe","Sword","Knife","Spear","Fireball(spell)","Frostball(spell)","Blink(spell)","Val'kyr(spell)"))
        #Lower damage for the knife 
        if type_wepon_or_spell=='Knife':
            damage=int(randint(1,60)//(random()+1))
        if 'spell' in type_wepon_or_spell:
            damage=randint(5,20)
            manna_cost=randint(5,15)
            cast_range=randint(2,4)
            self.found_loot=Spell(type_wepon_or_spell,damage,manna_cost,cast_range)
        else:
            self.found_loot=Weapon(type_wepon_or_spell,damage)

    def found_loot_obj(self):
        return self.found_loot

    def __str__(self):
        return self.found_loot.get_name()
