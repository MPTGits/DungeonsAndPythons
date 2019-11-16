from Dungeon.dungeon import *
from sty import fg, bg, ef, rs
import os

def game_loop():
    DungeonGenerator(20,20,'lvl.txt')
    dungeon = Dungeon('lvl.txt')
    print(fg(9)+ef.blink+'Hello player,welcome to dungeon and pythons!'+rs.blink+rs.fg)
    hero_name=input('Insert your heros name:')
    hero_known_as=input('How do you want your hero to be known as:')
    print(fg(9)+'Let your adventure begin {} the {},here,you can have a Fireball spell and Axe of Anger,although I doubt they will help!'.format(hero_name,hero_known_as))
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
        # check_weapon = False
        # if enemy1 is not False:
        #     print(dungeon.get_enemy_position(enemy1))
        #     dungeon.move_enemy('up')
        if enemy1 is False and enemy2 is False:
            continue
        if enemy2 is False:
            fight = Fight(hero, enemy1, dungeon)
            enemy = enemy1
        else:
            fight = Fight(hero, enemy2, dungeon)
            enemy = enemy2
        helper = False
        while enemy.is_alive() is True and hero.is_alive() is True:
            if helper is False:
                fight.attack_by_hero()
                helper = True
            else:
                if dungeon.enemy_attack(enemy) is True:
                    fight.attack_by_enemy()
                else:
                    print('Enemy moves')
                    dungeon.move_enemy(enemy)
                    dungeon.print_map()
                    time.sleep(2)
                helper = False
        if enemy.is_alive() is False:
            enemy_x=dungeon.get_enemy_position(enemy)[0]
            enemy_y=dungeon.get_enemy_position(enemy)[1]
            dungeon.kill_enemy(enemy,enemy_x,enemy_y)
        if hero.is_alive() is False:
            print(fg(9)+ef.blink+'LOSER!'+rs.blink+rs.fg)
            break


def main():
    DungeonGenerator(37,60,'lvl.txt')
    view=Dungeon('lvl.txt')
    me=Hero('Marto', 'The God', 99, 99,5)
    view.spawn(me)
    game_loop()

if __name__ == '__main__':
    main()


