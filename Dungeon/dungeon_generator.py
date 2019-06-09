from random import random,randint
from sty import fg, bg, ef, rs
import sys
from Charecters.hero import Hero
from Charecters.enemy import Enemy
from Items.treasure import Treasure
from Items.weapon import Weapon
from Items.spell import Spell

class DungeonGenerator:

    def __init__(self,height,width,file_name):
        self.height=height
        self.width=width
        self.room_cordinates = []
        self.dungeon = []
        self.created_rooms_cordinates=[]
        self.file_name=file_name

        #Generating a dungeon of only walls
        for h in range(self.height):
            row = []
            for w in range(self.width):
                row.append('#')
            self.dungeon.append(row)
        self.init()

#init method to creat all of the main map and parse everything to a file
    def init(self):
        self.split_rooms(1,1,self.height-1,self.width-1)
        self.create_rooms()
        self.create_coridoors()
        self.parse_dungeon_lst_to_file()

    #This method splits our dungeon(matrix) into portions of rooms
    #if we get a room that size is smaller then the size we seek we add those cordinates to our room_list
    #(room_starting_row,room_starting_col,room_end_row,room_end_col)

    #Max give us the an idea of how large we want our rooms to be
    def split_rooms(self, min_row, min_col, max_row, max_col,MAX_SIZE=18):
        room_height = max_row - min_row
        room_width = max_col - min_col
        

        if room_height < MAX_SIZE and room_width < MAX_SIZE:
            self.room_cordinates.append((min_row, min_col, max_row, max_col))
        elif room_height < MAX_SIZE and room_width >= MAX_SIZE:
            self.split_vertical(min_row, min_col, max_row, max_col)
        elif room_height >= MAX_SIZE and room_width < MAX_SIZE:
            self.split_horizontal(min_row, min_col, max_row, max_col)
        else:
            if random()>0.5:
                self.split_horizontal(min_row, min_col, max_row, max_col)
            else:
                self.split_vertical(min_row, min_col, max_row, max_col)

#Dividing the room by two and adding a bit to it so we have some rooms on diffrent rows and cols and with diffrent shapes
    def split_horizontal(self, min_row, min_col, max_row, max_col):
        split = (min_row + max_row) // 2+randint(-3,3)
        self.split_rooms(min_row, min_col, split, max_col)
        self.split_rooms(split + 1, min_col, max_row, max_col)

    def split_vertical(self, min_row, min_col, max_row, max_col):
        split = (min_col + max_col) // 2+randint(-3,3 )
        self.split_rooms(min_row, min_col, max_row, split)
        self.split_rooms(min_row, split + 1, max_row, max_col)

    #Creating rooms by cordinates
    def create_rooms(self):
        for room_cordinate in self.room_cordinates:
            #Skiping some of the rooms so it dosen't look too monotonical
            if random()>0.7:
                continue
            #We want to make the actual size of the room be around 70-90% of the expected size
            #so things look a bit more interesting 
            room_height=int(randint(70,90)/100*(room_cordinate[2]-room_cordinate[0]))
            room_width=int(randint(70,90)/100*(room_cordinate[3]-room_cordinate[1]))
            room_row_start=room_cordinate[0]
            room_col_start=room_cordinate[1]

            self.created_rooms_cordinates.append((room_row_start,room_col_start,room_row_start+room_height,room_col_start+room_width))
            for x in range(room_row_start,room_row_start+room_height):
                for y in range(room_col_start,room_col_start+room_width):
                    self.dungeon[x][y]='.'
#Connecting every center of a room with the room next in the list of rooms,that way we will have a path from the first
#room all the way to the last one
    def create_coridoors(self):
        for index in range(len(self.created_rooms_cordinates)-1):
            center_room1 = [(self.created_rooms_cordinates[index][2]+self.created_rooms_cordinates[index][0])//2, (self.created_rooms_cordinates[index][3]+self.created_rooms_cordinates[index][1])//2]
            center_room2=[(self.created_rooms_cordinates[index+1][2]+self.created_rooms_cordinates[index+1][0])//2, (self.created_rooms_cordinates[index+1][3]+self.created_rooms_cordinates[index+1][1])//2]
            
            #First we built the path by the x cordinate
            while abs(center_room1[0]-center_room2[0])!=0:
                if center_room1[0]-center_room2[0]>0:
                    self.dungeon[center_room2[0]][center_room2[1]]='.'
                    self.dungeon[center_room2[0]][center_room2[1]+1]='.'
                    center_room2[0]+=1
                else:
                    self.dungeon[center_room1[0]][center_room1[1]]='.'
                    self.dungeon[center_room1[0]][center_room1[1]+1]='.'
                    center_room1[0]+=1
            #One more iteration after the cycle so we get the last value
            self.dungeon[center_room1[0]][center_room1[1]]='.'
            self.dungeon[center_room1[0]][center_room1[1]+1]='.'
            #Second we built the path by the y cordinate
            while abs(center_room1[1]-center_room2[1])!=0:
                if center_room1[1]-center_room2[1]>0:
                    self.dungeon[center_room2[0]][center_room2[1]]='.'
                    self.dungeon[center_room2[0]+1][center_room2[1]]='.'
                    center_room2[1]+=1
                else:
                    self.dungeon[center_room1[0]][center_room1[1]]='.'
                    self.dungeon[center_room1[0]+1][center_room1[1]]='.'
                    center_room1[1]+=1
            #One more iteration after the cycle so we get the last value
            self.dungeon[center_room1[0]][center_room1[1]]='.'
            self.dungeon[center_room1[0]+1][center_room1[1]]='.'

#Parsing our final version of the generated dungeon to a text file
    def parse_dungeon_lst_to_file(self):
        with open(self.file_name,'w+') as f:
            self.generate_health_pots()
            self.mark_exit_area()
            self.parse_treasures_to_file()
            self.spawn_enemies()
            self.parse_color_file()
            f.write(str(self.dungeon))
#We mark our exit from the dungeon
    def mark_exit_area(self):
        for r in range(self.height-1):
                for c in range(self.width-1):
                    if self.dungeon[self.height-1-r][self.width-1-c]=='.':
                        self.dungeon[self.height-1-r][self.width-1-c]='G'
                        self.dungeon[self.height-1-r][self.width-2-c]='G'
                        return 


    #Parsing all the treasures to a file so we can add them latter to our dungeon
    def parse_treasures_to_file(self,treasure_file='treasure.txt'):
        with open(treasure_file,'w') as f:
            treasures=2
            while treasures>0:
                random_x=randint(0,self.height-1)
                random_y=randint(0,self.width-1)
                if self.dungeon[random_x][random_y]=='.' :
                    loot=Treasure()
                    if isinstance(loot.found_loot_obj(),Weapon):
                        f.write(loot.found_loot_obj().get_name()+' '+str(loot.found_loot_obj().get_damage())+'\n')
                    else:
                        f.write(loot.found_loot_obj().get_name()+' '+str(loot.found_loot_obj().get_damage())+' '+str(loot.found_loot_obj().get_mana_cost())+' '+str(loot.found_loot_obj().get_cast_range())+'\n')
                    self.dungeon[random_x][random_y]='T'
                    treasures-=1

    #Method that spawns enemies at random places on the map
    def spawn_enemies(self,enemies_file='enemies.txt'):
        with open(enemies_file,'w') as f:
            enemies=randint(4,8)
            if (self.height<30 or self.width<30):
                enemies=enemies//2
            while enemies>0:
                random_x=randint(3,self.height-1)
                random_y=randint(0,self.width-1)
                if self.dungeon[random_x][random_y]=='.':
                    health=randint(20,100)
                    mana=randint(10,50)
                    damage=randint(5,20)
                    if self.height<30 and self.width<30:
                        health=int(health/2)
                        mana=int(mana/2)
                        damage=int(damage/2)
                    f.write(str(health)+' '+str(mana)+' '+str(damage)+' '+str(random_x)+' '+str(random_y)+'\n')
                    self.dungeon[random_x][random_y]='E'
                    enemies-=1
#Generates pots
    def generate_health_pots(self):
        x=randint(0,self.height-1)
        y=randint(0,self.width-1)
        if self.dungeon[x][y]=='.':
            self.dungeon[x][y]='+'
    #We save the colors used for our map in a file so we don't get a diffrent random color map when we refresh the movement
    def parse_color_file(self,color_file='color.txt'):
        with open(color_file,'w') as f:
            for r in range(self.height):
                for c in range(self.width):
                    color_decider=randint(0,25)
                    f.write(str(color_decider)+'\n')

    #Not a nesesary method at this point
    @property
    def get_str_representation(self):
        rows = ''
        for r in range(self.height):
            for c in range(self.width):
                color_decider=randint(0,25)
                if self.dungeon[r][c]=='#':
                    if color_decider<=8:
                        rows+= fg(22)+bg(22)+self.dungeon[r][c]+rs.bg
                    elif color_decider>12 and color_decider<=20:
                        rows+= fg(236)+bg(236)+self.dungeon[r][c]+rs.bg
                    else:
                        rows+= fg(237)+bg(237)+self.dungeon[r][c]+rs.bg
                else:
                    if color_decider<=14:
                        rows+= fg(242)+bg(242)+self.dungeon[r][c]+rs.bg
                    elif color_decider>14 and color_decider<=20:
                        rows+= fg(243)+bg(243)+self.dungeon[r][c]+rs.bg
                    else:
                        rows+= fg(244)+bg(244)+self.dungeon[r][c]+rs.bg
            rows+='\n'
        return rows


# obj=DungeonGenerator(37,60)
# obj.split_rooms(1,1,36,59)
# obj.create_rooms()
# obj.create_coridoors()
# print(obj.get_str_representation)
