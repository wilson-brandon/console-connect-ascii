# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:18:31 2022

@author: wilsonbr

Console Connect Four
"""

import os, time

# Game Classes and Functions 

class Grid:
    def __init__(self, blankspace):
        self.blank = blankspace # character for empty grid spaces
        self.rows = 6         # grid rows
        self.columns = 7      # grid columns
        self.grid = [[self.blank for i in range(self.columns)]\
                     for j in range(self.rows)] # building grid
        self.isFull = False
        self.isFour = False 
  
    def displayGrid(self): 
        """Prints out playing grid"""
        headcount = 1
        header = []
        for i in range(self.columns): #filling header list
            header.append(str(headcount))
            headcount += 1
        print('\n')
        print(' |','   '.join(header),'|') # convert header to string, print
        for i in range(self.rows):
             print(' |','   '.join(self.grid[i]),'|') # print rows as string

    def fullGridCheck(self):
        """Returns True if grid top row is full (board is full)"""
        for i in self.grid[0]:
            if self.grid[0][i] == self.blank:
                return
        self.isFull = True
        return

    def playPiece(self, col, player, playerkey): 
        """Plays a piece and updates the grid 
        Args = int column, P1/P2 bool, player dictionary"""
        os.system('cls||clear') # clear the console, cleans up play
        blanks = 0 
        piece = playerkey[player][0] 
        for i in range(self.rows):
            if self.grid[i][col] == self.blank:  
                blanks += 1 # adding up number of blank spaces in column
        self.grid[blanks - 1][col] = piece # placing piece
        return self.grid
    
    def vertCheck(self, player, playerkey):
        """Checking for a vertical connect four"""
        count = 0
        piece = playerkey[player][0]
      
        for j in range (self.columns): # going across columns
            # Next column if < 3 pieces in col
            if self.grid[3][j] == self.blank: 
                continue
            else:
                for i in range (self.rows): # scanning down columns
                    if self.grid[i][j] == piece:
                        count += 1
                        if count >= 4: # four in a row
                            self.isFour = True   
                            return
                    else:
                        count = 0 # reset count if blank space 
        if count >= 4:
            self.isFour = True
            
    def horizCheck(self, player, playerkey):
        """Checking for a horizontal connect four"""
        count = 0
        piece = playerkey[player][0]
        for i in range (self.rows): 
            for j in range (self.columns): # scanning across columns
                if self.grid[i][j] == piece:
                    count += 1
                    if count >= 4:
                        self.isFour = True   
                        return
                else:
                    count = 0 # reset count if blank space 
        if count >= 4:
            self.isFour = True
            
    def diagCheck(self, player, playerkey):
        """ Checking for a diagonal connect four """
        piece = playerkey[player][0]
        
        # Check Down Right Diagonals
        count = 0
        t = 0 # start from top left
        while (t <= 3): # iterate over columns
            i = 0
            # iterate through diagonal
            while ((i <= self.rows-1) and (t+i <= self.columns-1)):
                if self.grid[i][t+i] == piece:
                    count += 1
                    i += 1
                    if count >= 4:
                        self.isFour = True
                        return
                else: # reset count and stop scanning this diagonal
                    count = 0
                    i += 1
            t += 1 # move to next column
            count = 0
       
        # Check Down Left Diagonals
        count = 0
        t = self.columns-1 #start from top right
        while (t >= 3):
            i = 0
            while ((i <= self.rows-1) and (t-i >= 0)):
                if self.grid[i][t-i] == piece:
                    count += 1
                    i += 1
                    if count >= 4:
                        self.isFour = True
                        return
                else:
                    count = 0
                    i += 1
            t -= 1 # move down to next row
            count = 0
        
        # Check Up Right Diagonals
        count = 0
        t = 0            
        while (t <= 3):
            j = self.rows - 1
            i = 0
            while ((j >= 0) and (t+i <= self.columns-1)):
                if self.grid[j][t+i] == piece:
                    count += 1
                    i += 1
                    j -= 1
                    if count >= 4:
                        self.isFour = True
                        return
                else:
                    count = 0
                    i += 1
                    j -= 1
            t += 1 # move up to next row
            count = 0
            
        # Check Up Left Diagonals
        count = 0
        t = self.columns-1            
        while (t >= 3):
            j = self.rows - 1
            i = 0
            while ((j >= 0) and (t-i >= 0)):
                if self.grid[j][t-i] == piece:
                    count += 1
                    i += 1
                    j -= 1
                    if count >= 4:
                        self.isFour = True
                        return
                else:
                    count = 0
                    i += 1
                    j -= 1
            t -= 1 # move up to next row
            count = 0
                
def changePlayer(player):
   """ Change player turn boolean """
   return not player

def validColumn(list, blankspace):
    """Return non-full columns"""
    indices = []
    for i in range(len(list)):
        if list[i] == blankspace:
            indices.append(i)
    return indices

def selectColumn():
    pass
            
def splash():
    """ Splash screen"""
    os.system('cls||clear') # clear the console
    s = """
    ###############################
    ###    ASCII Connect Four   ###
    ###     by Brandon Wilson   ###
    ###           2022          ### 
    ############################### """
    print(s)
    time.sleep(3)
    os.system('cls||clear')

# Game Settings

blankSpace = '-' # grid blank space character
gameGrid = Grid(blankSpace) # grid class instance
playerkey = {
    True: ['O','Player 1'], 
    False: ['X', 'Player 2']
    } #piece and player dictionary
player1 = False  # turn boolean, needs to default at False
gameTurn = 1 #Turn number

# Game Loop

splash()
gameGrid.displayGrid()
while gameGrid.isFour == 0 and gameGrid.isFull == 0:
    player1 = changePlayer(player1) # change players
    
    # Player input 
    valid_cols = set(validColumn(gameGrid.grid[0], blankSpace))
    while True:
        col_prompt = 'please select column to drop piece...'
        print('\nTurn',gameTurn,'.',playerkey[player1][1], \
            '(',playerkey[player1][0], ')',col_prompt)
        input_col = int(input())-1 # user input column

        # Check if column isn't full
        if input_col in valid_cols:
            break
        else:
            gameGrid.displayGrid()
            print('\nColumn is full, choose another!')
            continue
    
    gameGrid.playPiece(input_col,player1,playerkey) # playing piece
    gameGrid.displayGrid() # printing board
    gameGrid.vertCheck(player1,playerkey) # check for vertical connect four
    gameGrid.horizCheck(player1,playerkey) # check for horiz connect four
    gameGrid.diagCheck(player1,playerkey) # check for diag connect four
    gameTurn += 1

if gameGrid.isFull: # grid completely filled
    print('Draw! Thanks for playing\n')

else: # victory message
    print('\n')
    print(playerkey[player1][1],'wins! Thanks for playing.\n')
    