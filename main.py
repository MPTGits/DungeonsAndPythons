from dungeon import *
from sty import fg, bg, ef, rs

def game_loop():
    DungeonGenerator(20,20,'lvl.txt')
    dungeon = Dungeon('lvl.txt')
    print(fg(9)+ef.blink+'Hello player,welcome to dungeon and pythons!'+rs.blink+rs.fg)
    hero_name=input('Insert your heros name:')
    hero_known_as=input('How do you want your hero to be known as:')
    print(fg(9)+'Let your adventure begin '+hero_name+' the '+ hero_known_as+',here,you can have a Fireball spell and Axe of Anger,although I doubt they will help!')
    hero = Hero(hero_name, hero_known_as, 99, 99,5)
    spell = Spell(name="Fireball", damage=15, mana_cost=50, cast_range=2)
    weapon = Weapon(name='Axe of Anger',damage=10)
    hero.equip(weapon)
    hero.learn(spell)
    dungeon.spawn(hero)
    while True:
        if dungeon.get_current_level()>3:
            print('GET READY FOR A BOSS FIGHT STAGE!')
            time.sleep(100)
        dungeon.print_map()
        move=input('Input move(w/a/s/d):')
        if move=='w':
            dungeon.move_hero('up')
        elif move=='s':
            dungeon.move_hero('down')
        elif move=='a':
            dungeon.move_hero('left')
        elif move=='d':
                dungeon.move_hero('right')
        enemy1 = dungeon.hero_attack(by="spell")
        enemy2 = dungeon.hero_attack(by="weapon")
        # if enemy1 is not False:
        #     print(dungeon.get_enemy_position(enemy1))
        #     dungeon.move_enemy('up')
        if enemy1 is False and enemy2 is False:
            continue
        if enemy2 is False:
            fight = Fight(hero, enemy1,dungeon)
            enemy = enemy1
            # fight.start()
        else:
            fight = Fight(hero, enemy2,dungeon)
            enemy = enemy2
            # fight.start()
        helper = False
        while enemy.is_alive() is True and hero.is_alive() is True:
            if helper is False:
                fight.attack_by_hero()
                helper = True
            else:
                if dungeon.enemy_attack(enemy) is True:
                    fight.attack_by_enemy()
                else:
                    pass#print('Enemy moves')
                    #Implemented this just to test things out it only works if hero starts to attack enemy from above
                    #(Delet this when you do the move method!)
                    #dungeon.set_enemy_position(enemy,dungeon.get_enemy_position(enemy)[0]-1,dungeon.get_enemy_position(enemy)[1])
                helper = False
        if enemy.is_alive() is False:
            enemy_x=dungeon.get_enemy_position(enemy)[0]
            enemy_y=dungeon.get_enemy_position(enemy)[1]
            dungeon.kill_enemy(enemy,enemy_x,enemy_y)



def main():
    DungeonGenerator(37,60,'lvl.txt')
    view=Dungeon('lvl.txt')
    me=Hero('Marto', 'The God', 99, 99,5)
    view.spawn(me)
    game_loop()

main()

#game_loop()

# TO DO
# move enemy
# to be able to step on enemy's position in order to fight with a weapon
#add mana on every step
# put attacks in different methods
