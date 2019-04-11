#pip3 install termcolor
#Librarry to have diffrent colors in console

from sty import fg, bg, ef, rs
from termcolor import colored
import random

#Example ussage of coloring
#print(colored('hello', 'red'), colored('world', 'green'))

class Dungeon_generator():
    #Size of map and number of iterations for the cellular automata to complete(the more iterations the smoother the map looks)
    #ideal iterations are 4-5
    def __init__(self,width,height,iterations):
        self.width=width
        self.height=height
        #self.regualr_iterations=regualr_iterations
        #self.final_dungeon=[]
        map_layout=self.__creat_layout()
        #Optimal chance of a wall is around 40%
        final_dungeon=self.__layout_populate(map_layout,43)
        for x in range(iterations):
            #Minimum count of 5 neighbours for a cell to become a wall is optimal
            final_dungeon=self.__cellular_iterations(final_dungeon,5)
        #initilizing the dungeong to the str representation
        self.final_dungeon=self.dungeon_to_str(final_dungeon,'#','.')


    def get_dungeon(self):
        return self.final_dungeon

    #A private method that creats our layout whic is simply a boolean matrix with its outer bounds structured by '1'
    #(which is our outline of the map)
    #PS:Sorry che e na angliiski ama me murzi da si sloja kirilica na Ubuntu-to :D 
    def __creat_layout(self):
        map_layout = [[0 for x in range(self.height)] for y in range(self.width)]
        map_layout[0]=[1 for x in range(self.width)]
        map_layout[len(map_layout)-1]=[1 for x in range(self.width)]
        for x in range(self.height):
            for y in range(self.width):
                if x==0 or y==0:
                    map_layout[x][y]=1
        return map_layout

    #A private method that populates the map layout with walls on random
    #(generates a random int and if its smaller by a given chance we make the pathway a wall)
    def __layout_populate(self,map_layout,chance):
        #In case a chance higher than 100% is entered
        chance=chance%100
        for x in range(self.height):
            for y in range(self.width):
                if random.randint(0,100)<chance:
                    map_layout[x][y]=1
        return map_layout

    #A private methdo which applies the cellular algorithm the main idea is:
    #We go through the procces of comparing all 8 neighbours of a given cell 
    #if there are more 'wall' neighbours than 'free space' neighbours we make that cell into a wall 
    #if not it reamains a free space
    #NOTE:The pillars are used when we have no neighbours that are walls we make the currecnt cell a wall
    #THIS METHOD ISNT GOOD FOR THE SPECIFIC DUNGEON GENERATOR IN THIS GAME SO I WON'T BE USING IT
    def __cellular_iterations(self,map_representation,min_count_neighbours,pillars=False):
        for x in range(self.height-1):
            for y in range(self.width-1):
                counter_neighbours=0
                for x1 in [1,0,-1]:
                    for y1 in [1,0,-1]:
                        if map_representation[x+x1][y+y1]==1:
                            counter_neighbours+=1
                if counter_neighbours>=min_count_neighbours or (counter_neighbours==0 and pillars==True):
                    map_representation[x][y]=1
                else:
                    map_representation[x][y]=0
        return map_representation
    
    #A initilizing method for the class
    def init(self):
       pass



    @classmethod
    #Just a method to pring our boolean matrix as a graphical dungeon
    def dungeon_to_str(cls,bool_dungeon,wall_char,free_space_char):
        str_representation = "\n"
        for i in range(len(bool_dungeon)-1):
            for j in range(len(bool_dungeon[0])-1):
                if bool_dungeon[j][i]==1:
                    p=random.randint(0,10)
                    #I am just using a library so I can color my char and background and the dungeon looks neat
                    #fg(int) is the color of the char and bg(int) is the background color
                    #reference to the github:https://github.com/feluxe/sty
                    if p<=3:
                        str_representation += fg(235)+bg(235)+wall_char+rs.bg
                    elif p>3 and p<=8:
                        str_representation += fg(236)+bg(236)+wall_char+rs.bg
                    else:
                        str_representation += fg(237)+bg(237)+wall_char+rs.bg
                else:
                    str_representation += fg(248)+bg(248)+free_space_char+rs.bg
            str_representation += "\n"
        str_representation += "\n"
        return str_representation


test_dungeong=Dungeon_generator(32,32,5)

print(test_dungeong.get_dungeon())