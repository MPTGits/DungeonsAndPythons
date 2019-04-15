from random import random,randint,choice
from sty import fg, bg, ef, rs
import sys
from hero import Hero
from treasure import Treasure
from enemy import Enemy
from hero import Weapon
from spell import Spell
from health_potion import HealthPotion
from random import randint,choice
import time
from dungeon_generator import DungeonGenerator
from fight import Fight


class Dungeon:

    def __init__(self,file_name):
        self.current_lvl=1
        self.file_name=file_name
        self.my_hero=None
        self.hero_position=(-1,-1)
        self.treasure_list=[]
        self.enemies_list=[]
        self.get_treasures()
        self.get_enemies_from_file()


#Refreshing mobs and treasures on the new dungeon
    def refresh_for_new_level(self):
        self.current_lvl+=1
        DungeonGenerator(int(20*self.current_lvl/2),20*self.current_lvl,'lvl.txt')
        self.enemies_list=[]
        self.get_enemies_from_file()
        self.treasure_list=[]
        self.get_treasures()
        self.spawn(self.my_hero)
    
    def get_current_level(self):
        return self.current_lvl

#saving the possiable treasures in the list from a file
    def get_treasures(self,treasure_file='treasure.txt'):
        with open(treasure_file,'r') as f:
            for line in f:
                gift=line.split(' ')
                if len(gift)>3:
                    self.treasure_list.append(Spell(gift[0],int(gift[1]),int(gift[2]),int(gift[3])))
                else:
                    self.treasure_list.append(Weapon(gift[0],int(gift[1])))
#saving enemise to the list as a list (enemy,x cordinate,ycordinate)
    def get_enemies_from_file(self,enemies_file='enemies.txt'):
        with open(enemies_file,'r') as f:
            for line in f:
                enemy=line.split(' ')
                enemy=list(map(int,enemy))
                self.enemies_list.append([Enemy(enemy[0],enemy[1],enemy[2]),enemy[3],enemy[4]])
#gives possition of given enemy if it is in the list of enemies
    def get_enemy_position(self,picked_enemy):
        for enemy in self.enemies_list:
            if enemy[0]==picked_enemy:
                return(enemy[1],enemy[2])
    
    #gets a list of all our enemmies on the map
    def get_list_of_enemies(self):
        enemy_list=[]
        for id in range(len(self.enemies_list)-1):
            enemy_list.append(self.enemies_list[id][0])
        return enemy_list



    def set_enemy_position(self,enemy_char,new_x_poss,new_y_poss):
        dungeon_lst=self.get_dungeon_lst()
        for idx in range(len(self.enemies_list)):
            if self.enemies_list[idx][0]==enemy_char:
                dungeon_lst[self.enemies_list[idx][1]][self.enemies_list[idx][2]]='.'
                self.enemies_list[idx][1]=new_x_poss
                self.enemies_list[idx][2]=new_y_poss
                if dungeon_lst[new_x_poss][new_y_poss]=='H':
                    break
                dungeon_lst[new_x_poss][new_y_poss]='E'
                break
        self.update_file(dungeon_lst)
#Makes enemy into a path symbol(deletes the enemy from the dungeon)
    def kill_enemy(self,enemy,x_poss,y_poss):
        dungeon_lst=self.get_dungeon_lst()
        if dungeon_lst[x_poss][y_poss]!='H':
            dungeon_lst[x_poss][y_poss]='x'
        self.enemies_list.remove([enemy,x_poss,y_poss])
        self.update_file(dungeon_lst)

    def get_hero_position(self):
        return self.hero_position

#return list of enemies that are in the dungeon
    def get_enemies(self):
        result_list = []
        for enemy in self.enemies_list:
            result_list.append(enemy[0])
        return result_list

#refreshes the file with the updates
    def update_file(self,new_list):
        with open(self.file_name,'w') as f:
            f.write(str(new_list))
#returns list layout of the dungeon
    def get_dungeon_lst(self):
        with open(self.file_name,'r') as f:
            lst=eval(f.read())
        return lst

    def print_map(self,color_file='color.txt'):
        with open(self.file_name,'r') as f,open(color_file,'r') as color_f:
            dungeon_lst=eval(f.read())
            
            for r in range(len(dungeon_lst)-1):
                rows = ''
                for c in range(len(dungeon_lst[0])-1):
                    color_decider=int(color_f.readline())
                    if dungeon_lst[r][c]=='#':
                        if color_decider<=8:
                            rows+= fg(22)+bg(22)+dungeon_lst[r][c]+rs.bg
                        elif color_decider>12 and color_decider<=20:
                            rows+= fg(236)+bg(236)+dungeon_lst[r][c]+rs.bg
                        else:
                            rows+= fg(237)+bg(237)+dungeon_lst[r][c]+rs.bg
                    elif dungeon_lst[r][c]=='.':
                        if color_decider<=14:
                            rows+= fg(242)+bg(242)+dungeon_lst[r][c]+rs.bg
                        elif color_decider>14 and color_decider<=20:
                            rows+= fg(243)+bg(243)+dungeon_lst[r][c]+rs.bg
                        else:
                            rows+= fg(244)+bg(244)+dungeon_lst[r][c]+rs.bg
                    elif dungeon_lst[r][c]=='H':
                        rows+= fg(216)+bg(216)+dungeon_lst[r][c]+rs.bg
                    elif dungeon_lst[r][c]=='T':
                        rows+= bg(214)+ef.blink+dungeon_lst[r][c]+rs.blink+rs.bg
                    elif dungeon_lst[r][c]=='E':
                        rows+= fg(88)+bg(88)+dungeon_lst[r][c]+rs.bg
                    elif dungeon_lst[r][c]=='G':
                        rows+= fg(16)+bg(16)+dungeon_lst[r][c]+rs.bg
                    elif dungeon_lst[r][c]=='+':
                        rows+=bg(9)+ef.blink+dungeon_lst[r][c]+rs.blink+rs.bg
                    else:
                        rows+=dungeon_lst[r][c]

                print(rows)


    def spawn(self,hero):
        self.my_hero=hero
        dungeon_lst=self.get_dungeon_lst()
        for r in range(len(dungeon_lst)-1):
            for c in range(len(dungeon_lst)-1):
                if dungeon_lst[r][c]=='.':
                    dungeon_lst[r][c]='H'
                    self.hero_position=(r,c)
                    self.update_file(dungeon_lst)
                    return True
        return False
    
#Method that does all the checking of the square that the hero is on
    def check_if_move_is_valid_and_make_it(self,x,y):
        dungeon_lst=self.get_dungeon_lst()
        r,c=self.hero_position
        print('Cordinates:',r+x,c+y)
        if dungeon_lst[r+x][c+y] =='G':
            self.refresh_for_new_level()
            return True
        elif (r+x >=0 and r+x<=len(dungeon_lst)-1) and (c+y>=0 and c+y<=len(dungeon_lst[0])-1) and (dungeon_lst[r+x][c+y]=='.' or dungeon_lst[r+x][c+y]=='T' or dungeon_lst[r+x][c+y]=='+'or dungeon_lst[r+x][c+y]=='x'):
            dungeon_lst[r][c]='.'
            if dungeon_lst[r+x][c+y]=='T':
                found_item=choice((self.treasure_list))
                print(str(found_item))
                if isinstance(found_item,Weapon):
                    self.my_hero.equip(found_item)
                else:
                    self.my_hero.learn(found_item)
                time.sleep(5)
            elif dungeon_lst[r+x][c+y]=='+':
                potion=HealthPotion(randint(5,15))
                print('Hero has reseved a heal of',potion.get_restored_health(),'HP')
                self.my_hero.take_healing(potion.get_restored_health())
            dungeon_lst[r+x][c+y]='H'
            self.hero_position=(r+x,c+y)
            self.update_file(dungeon_lst)
            return True
        return False


    def move_hero(self,direction):
        if direction=='up':
            self.check_if_move_is_valid_and_make_it(-1,0)
        elif direction=='down':
            self.check_if_move_is_valid_and_make_it(1,0)
        elif direction=='right':
            self.check_if_move_is_valid_and_make_it(0,1)
        elif direction=='left':
            self.check_if_move_is_valid_and_make_it(0,-1)
        self.my_hero.set_mana(self.my_hero.get_mana_regen_rate())

# check if the hero can attack by weapon and spell, not tested
    def hero_attack(self, by=""):
        if by == "weapon":
            if self.my_hero.can_attack_by_weapon() is False:
                return False
            for enemy in self.get_enemies():
                #print(self.get_hero_position(),self.get_enemy_position(enemy))
                if self.get_hero_position() == self.get_enemy_position(enemy):
                    return enemy
            return False
        else:
            for enemy in self.get_enemies():
                if self.get_hero_position() == self.get_enemy_position(enemy):
                    return enemy
            cast_range = self.my_hero.spell.get_cast_range()
            dungeon_lst = self.get_dungeon_lst()
            rows_hero = self.hero_position[0]
            col_hero = self.hero_position[1]
            right = (rows_hero, col_hero + cast_range)
            left = (rows_hero, col_hero - cast_range)
            up = (rows_hero - cast_range, col_hero)
            down = (rows_hero + cast_range, col_hero)
            for enemy in self.get_enemies():
                enemy_pos = self.get_enemy_position(enemy)
                if enemy_pos[0] == right[0] and enemy_pos[1] <= right[1] and enemy_pos[1] >= col_hero:
                    return enemy
                if enemy_pos[0] == left[0] and enemy_pos[1] >= left[1] and enemy_pos[1] <= col_hero:
                    return enemy
                if enemy_pos[1] == up[1] and enemy_pos[0] >= up[0] and enemy_pos[0] <= rows_hero:
                    return enemy
                if enemy_pos[1] == down[1] and enemy_pos[0] <= down[0] and enemy_pos[0] >= rows_hero:
                    return enemy
        return False


    def enemy_attack(self, enemy):
        if self.get_hero_position() == self.get_enemy_position(enemy):
            return True
    #     else:
            # moves closer to hero



#This is the way to save our dungeon to a file with our dungeon generator(by only calling the class with height and width of map and a file
#to save it to
# DungeonGenerator(37,60,'lvl.txt')
# view=Dungeon('lvl.txt')
# me=Hero('Marto', 'The God', 99, 99,5)
# view.spawn(me)
# view.game_loop()

# # view.game_loop()


#     def game_loop(dungeon):
#         while True:
#             move=input('Input move(w/a/s/d):')
#             if move=='w':
#                 dungeon.move_hero('up')
#             elif move=='s':
#                 dungeon.move_hero('down')
#             elif move=='a':
#                 dungeon.move_hero('left')
#             elif move=='d':
#                 dungeon.move_hero('right')
#             dungeon.print_map()
    #         view.get_hero_position()
    #         print("something")
    #         for enemy in view.get_enemies():
    # # print(enemy)
    #             print(view.get_enemy_position(enemy))



# #while True:
#     #pick=choice(('left','right','up','down'))
#     #view.move_hero(pick)
# # view.move_hero('down')
# # view.move_hero('down')
# # view.move_hero('down')
# # view.move_hero('down')
# for x in range(5):
#     view.move_hero('right')
