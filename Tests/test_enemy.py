import unittest 
import enemy

class testEnemyChars(unittest.TestCase):
    
    def test_name_generator(self):
        self.assertEqual(len(enemy.generate_word(5)),5)
        self.assertEqual(type(enemy.generate_word(5)),type(''))

    def test_negative_inputs_for_enemy_mob(self):
        #Digits at the end are (health,mana,damage)
        self.failUnlessRaises(Exception,enemy.Enemy,2,-4,6)
        self.failUnlessRaises(Exception,enemy.Enemy,-2,4,-6)

    def test_get_health_method(self):
        self.assertEqual(enemy.Enemy(3,3,3).is_alive(),True)
        self.assertEqual(enemy.Enemy(0,3,3).is_alive(),False)
        test_enemy=enemy.Enemy(4,5,2)
        test_enemy.take_damage(6)
        self.assertEqual(test_enemy.is_alive(),False)

    def test_get_mana_method(self):
        self.assertEqual(enemy.Enemy(3,2,3).can_cast(),True)
        self.assertEqual(enemy.Enemy(0,0,3).can_cast(),False)
        test_enemy=enemy.Enemy(2,4,100)
        test_enemy.take_mana(10)
        self.assertEqual(test_enemy.can_cast(),False)

    def test_take_healing_method(self):
        test_enemy=enemy.Enemy(2,4,100)
        test_enemy.take_healing(48)
        self.assertEqual(test_enemy.get_health(),50)
        test_enemy.take_healing(-48)
        self.assertEqual(test_enemy.get_health(),50)

    def test_attack_method(self):
        test_enemy=enemy.Enemy(2,4,100)
        lower_bound=test_enemy.get_damage()-test_enemy.get_damage()/10
        upper_bound=test_enemy.get_damage()
        self.assertTrue(lower_bound<test_enemy.attack(),upper_bound)



if __name__=='__main__':
    unittest.main()