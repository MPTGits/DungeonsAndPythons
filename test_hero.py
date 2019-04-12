import unittest
from hero import *

class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Bron", "Dragonslayer", 100, 100, 2)

    def test_hero_init(self):
        test_weapon = Weapon("",0)
        self.assertEqual(self.hero._name,"Bron")
        self.assertEqual(self.hero._title, "Dragonslayer")
        self.assertEqual(self.hero._health, 100)
        self.assertEqual(self.hero._mana, 100)
        self.assertEqual(self.hero._mana_regeneration_rate, 2)
        self.assertEqual(self.hero._max_health, 100)
        self.assertEqual(self.hero._max_mana, 100)
        self.assertEqual(self.hero._weapon, test_weapon)

    def test_hero_known_as(self):
        self.assertEqual(self.hero.known_as(), "Bron the Dragonslayer")

    def test_if_get_health_returns_health(self):
        self.assertEqual(self.hero.get_health(), 100)

    def test_if_get_mana_returns_mana(self):
        self.assertEqual(self.hero.get_mana(), 100)

    # def test_if_is_alive_returns_true_when_health_is_not_zero(self):
    #     self.assertEqual(self.hero.is_alive(), True)

    # def test_if_is_alive_returns_false_when_health_is_zero(self):
    #     self.hero2 = Hero("Bron", "Dragonslayer", 0, 100, 2)
    #     self.assertEqual(self.hero2.is_alive(), False)

    # def test_if_can_cast_returns_true_when_mana_is_not_zero(self):
    #     self.assertEqual(self.hero.can_cast(), True)

    # def test_if_can_cast_returns_false_when_mana_is_zero(self):
    #     self.hero2 = Hero("Bron", "Dragonslayer", 0, 0, 2)
    #     self.assertEqual(self.hero2.can_cast(), False)

    def test_is_alive(self):
        self.assertEqual(self.hero.is_alive(), True)
        self.hero2 = Hero("Bron", "Dragonslayer", 0, 100, 2)
        self.assertEqual(self.hero2.is_alive(), False)

    def test_can_cast(self):
        self.assertEqual(self.hero.can_cast(), True)
        self.hero2 = Hero("Bron", "Dragonslayer", 0, 0, 2)
        self.assertEqual(self.hero2.can_cast(), False)

    def test_use_mana(self):
        self.assertEqual(self.hero.use_mana(50), True)
        self.assertEqual(self.hero._mana, 50)
        self.assertEqual(self.hero.use_mana(100), False)
        self.assertEqual(self.hero._mana, 50)

    def test_take_damage(self):
        self.hero.take_damage(50)
        self.assertEqual(self.hero._health, 50)
        self.hero.take_damage(100)
        self.assertEqual(self.hero._health, 0)

    def test_take_healing(self):
        self.hero2 = Hero("Bron", "Dragonslayer", 0, 0, 2)
        self.assertEqual(self.hero2.take_healing(10), False)
        # self.hero.take_healing(150)
        self.assertEqual(self.hero.take_healing(200), True)
        self.assertEqual(self.hero.get_health(), 100)

    def test_take_mana(self):
        self.hero.take_mana()
        self.assertEqual(self.hero._mana, 100)
        self.hero.use_mana(50)
        self.hero.take_mana()
        self.assertEqual(self.hero._mana, 52)
        self.hero.take_mana(20)
        self.assertEqual(self.hero._mana, 72)
        self.hero.take_mana(50)
        self.assertEqual(self.hero._mana, 100)

    def test_equip(self):
        self.test_weapon = Weapon("Fireball", 100)
        self.hero.equip(self.test_weapon)
        self.assertEqual(self.hero._weapon, self.test_weapon)





if __name__ == '__main__':
    unittest.main()

