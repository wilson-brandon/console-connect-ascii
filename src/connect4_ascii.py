# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:18:31 2022

@author: wilsonbr

Console Connect Four
"""

### Game Functions ###

class Grid:
    def __init__(self, row, col, blankspace):
        self.blank = blankspace # character for empty grid spaces
        self.rows = row         # grid rows
        self.columns = col      # grid columns
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
        """Checks if top row is full (board is full)"""
        for i in self.grid[0]:
            if self.grid[0][i] == self.blank:
                return 0
        return 1

    def playPiece(self, col, player, playerkey): 
        """Plays a piece. Integer column, P1/P2 boolean, player dictionary"""
        blanks = 0 
        piece = playerkey[player][0] 
        for i in range(self.rows): # looping through column to count blanks
            if self.grid[i][col] == self.blank:  
                blanks += 1 # adding up number of blank spaces in column
        self.grid[blanks - 1][col] = piece # placing piece
        return self.grid
    
    def vertCheck(self, player, playerkey):
        """Checking for a vertical connect four"""
        count = 0
        piece = playerkey[player][0]
        for j in range (self.columns): 
            for i in range (self.rows): # scanning down columns
                if self.grid[i][j] == piece:
                    count += 1
                    if count >= 4:
                        self.isFour = True   
                        return
                else:
                    count = 0 # reset count if blank space 
        if count >= 4:
            self.isFour = True 
            
    def horizCheck(self, player, playerkey):
        """Checking for a vertical connect four"""
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
                    
def changePlayer(player):
   """Change player turn boolean"""
   if player == True:
       return False
   else:
       return True

### Initialize the game ###

# Set board dimensions and blank space char
rows = 6
columns = 7
blankSpace = '-'

# Initialize
gameGrid = Grid(rows,columns,blankSpace) # grid class instance
gameGrid.displayGrid()
playerkey = {
    True: ['O','Player 1'], 
    False: ['X', 'Player 2']
    } #piece and player dictionary
player1 = False  # turn boolean, needs to default at False
gameTurn = 1 #Turn number


### Play ###

while gameGrid.isFour == 0 and gameGrid.isFull == 0:
    player1 = changePlayer(player1) # change players
    
    # Column select prompt
    print('\n')
    col_prompt = 'please select column to drop piece...'
    print('Turn',gameTurn,'.',playerkey[player1][1], col_prompt)
    input_col = int(input())-1 # user input column
    
    gameGrid.playPiece(input_col,player1,playerkey) # playing piece
    gameGrid.displayGrid() # printing board
    gameGrid.vertCheck(player1,playerkey)
    gameGrid.horizCheck(player1,playerkey)
    gameTurn += 1
""
if gameGrid.isFull == 1:
    print('Draw! Thanks for playing')
else:
    print('\n')
    print(playerkey[player1][1],'wins! Thanks for playing.')
""
