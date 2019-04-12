from dungeon import *

def game_loop():
    DungeonGenerator(37,60,'lvl.txt')
    dungeon = Dungeon('lvl.txt')
    hero = Hero('Marto', 'The God', 99, 99,5)
    spell = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
    me.learn(spell)
    dungeon.spawn(me)
    # game_loop(dungeon)
    while True:
        move=input('Input move(w/a/s/d):')
        if move=='w':
            dungeon.move_hero('up')
        elif move=='s':
            dungeon.move_hero('down')
        elif move=='a':
            dungeon.move_hero('left')
        elif move=='d':
            dungeon.move_hero('right')
        dungeon.print_map()
        # enemy1 = dungeon.hero_attack(by="spell")
        # enemy2 = dungeon.hero_attack(by="weapon")
        # # if enemy1 is not False:
        # #     print(dungeon.get_enemy_position(enemy1))
        # #     dungeon.move_enemy('up')
        # if enemy1 is False and enemy2 is False:
        #     continue
        # if enemy2 is False:
        #     fight = Fight(hero, enemy1)
        #     enemy = enemy1
        #     # fight.start()
        # else:
        #     fight = Fight(hero, enemy2)
        #     enemy = enemy2
        #     # fight.start()
        # helper = False
        # while enemy.is_alive() is True and hero.is_alive() is True:
        #     if helper is False:
        #         fight.attack_by_hero()
        #         helper = True
        #     else:
        #         if dungeon.enemy_attack(enemy) is True:
        #             fight.attack_by_enemy()
        #         else:
        #             move_enemy()
        #         helper = False



# def main():
#     DungeonGenerator(37,60,'lvl.txt')
#     view=Dungeon('lvl.txt')
#     me=Hero('Marto', 'The God', 99, 99,5)
#     view.spawn(me)
#     game_loop(view)

# main()

game_loop()

# TO DO
# move enemy
# to be able to step on enemy's position in order to fight with a weapon
#add mana on every step
# put attacks in different methods