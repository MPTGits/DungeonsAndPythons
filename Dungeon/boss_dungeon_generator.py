from sty import fg, bg, ef, rs
from termcolor import colored
import random

#THIS IS A 'CAVE STYLE' DUNGEON GENERATOR FOR THE BOSS FIGHTS,MOST LIKELY WON'T HAVE TIME TO IMPLEMENT IT IN THE GAME THO

class Boss_dungeon_generator():
    #Size of map and number of iterations for the cellular automata to complete(the more iterations the smoother the map looks)
    #ideal iterations are 4-5
    def __init__(self,width,height,iterations=5):
        self.width=width
        self.height=height
        #self.regualr_iterations=regualr_iterations
        #self.final_dungeon=[]
        map_layout=self.__creat_layout()
        #Optimal chance of a wall is around 40%
        self.final_dungeon=self.__layout_populate(map_layout,40)
        for x in range(iterations):
            #Minimum count of 5 neighbours for a cell to become a wall is optimal
            self.final_dungeon=self.__cellular_iterations(self.final_dungeon,5)

    #A private method that creats our layout whic is simply a boolean matrix with its outer bounds structured by '1'
    #(which is our outline of the map)
    def __creat_layout(self):
        map_layout = [['.' for x in range(self.height)] for y in range(self.width)]
        map_layout[0]=['#' for x in range(self.width)]
        map_layout[len(map_layout)-1]=['#' for x in range(self.width)]
        for x in range(self.height):
            for y in range(self.width):
                if x==0 or y==0:
                    map_layout[x][y]='#'
        return map_layout

    #A private method that populates the map layout with walls on random
    #(generates a random int and if its smaller by a given chance we make the pathway a wall)
    def __layout_populate(self,map_layout,chance):
        #In case a chance higher than 100% is entered
        chance=chance%100
        for x in range(1,self.height-1):
            for y in range(1,self.width-1):
                if random.randint(0,100)<chance:
                    map_layout[x][y]='#'
        return map_layout

    #A private methdo which applies the cellular algorithm the main idea is:
    #We go through the procces of comparing all 8 neighbours of a given cell 
    #if there are more 'wall' neighbours than 'free space' neighbours we make that cell into a wall 
    #if not it reamains a free space
    #NOTE:The pillars are used when we have no neighbours that are walls we make the currecnt cell a wall
    #THIS METHOD ISNT GOOD FOR THE SPECIFIC DUNGEON GENERATOR IN THIS GAME SO I WON'T BE USING IT
    def __cellular_iterations(self,map_representation,min_count_neighbours,pillars=False):
        for x in range(1,self.height-1):
            for y in range(1,self.width-1):
                counter_neighbours=0
                for x1 in [1,0,-1]:
                    for y1 in [1,0,-1]:
                        if map_representation[x+x1][y+y1]=='#':
                            counter_neighbours+=1
                if counter_neighbours>=min_count_neighbours or (x==1 or y==1 or x==self.height-2 or (y==self.width-2 and x<self.height//1.2)):
                    map_representation[x][y]='#'
                else:
                    map_representation[x][y]='.'
        return map_representation
    
    #A getter for the dungeon
    def get_map(self):
        return self.final_dungeon

# test_dungeong=Boss_dungeon_generator(30,30)
