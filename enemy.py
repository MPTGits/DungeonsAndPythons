import random
from random_name_generator import *
#Random name generrator for enemy mobs 


class Enemy:
    def __init__(self,health ,mana,damage):
        if health<0 or mana<0 or damage<0:
            raise Exception("Your enemy cannot have neggative attributes!")
        self.health=health
        self.mana=mana
        self.damage=damage
        #Generates a random name that is between 4 and 7 chars long 
        self.name=generate_word(random.randint(4,7))

    def __str__(self):
        return "Creature:"+self.name
    
    def get_damage(self):
        return self.damage

    def is_alive(self):
        return self.health>0

    def can_cast(self):
        return self.mana>0

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self,healing_taken):
        if (self.is_alive() and healing_taken>0):
            self.health+=healing_taken
            return True
        return False 

    def take_mana(self,mana_taken):
            if(self.can_cast() and mana_taken>0):
                self.mana=max(0,self.mana-mana_taken)

    def attack(self):
        randomized_atack=random.randint(self.damage-self.damage/10,self.damage)
        return randomized_atack
    
    def take_damage(self,damage_taken):
        if (self.is_alive()):
            self.health=max(0,self.health-damage_taken)

    def __eq__(self,other):
        return self.health==other.health and self.mana==other.mana and self.damage==other.damage


