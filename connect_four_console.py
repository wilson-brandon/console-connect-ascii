# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:18:31 2022

@author: wilsonbr

Console Connect Four
"""

### Game Functions ###

def initGrid(): #initializing 2D array 
    grid4 = []
    for i in range(6): # 6 rows
        grid4.append(['_','_','_','_','_','_','_']) # 7 cols
    return grid4

def displayGrid(grid): #format, transpose and display grid in a nice way
   header1 = ['1', '2', '3', '4', '5', '6','7'] # column headers
   print('\n')
   print(header1) 
   print('\n')
   for i in range(6):
        print(grid[i])
   print('____________________________________')

def playPiece(grid, col, player, playerDict): 
   # grid array, col integer, player1 turn boolean, player piece dictionary
   blanks = 0 
   for i in range(6): #looping through column to find unoccupied space
       if grid[i][col] == '_':  
           blanks += 1 #adding up number of blank spaces in column
   grid[blanks-1][col] = playerDict[player][0] #placing piece
   return grid  

def changePlayer(player): # flip player turn boolean
    if player == True:
        player = False
    else:
        player = True
    return player

def fullGridCheck(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '_':
                return 0
    return 1    
    
#def checkColFull(grid)  
#def horizCheck():
#def diagcheck():
def vertCheck(grid, player, playerDict): #checks for vertical connect four
    count = 0
    for j in range(len(grid[0])): #scan across vertical columns
        for i in range(len(grid)): #scan down the column
            if grid[i][j] == playerDict[player][0]: #counts matching pieces
                count += 1 
            else:
                count = 0
        if count >= 4: #break out the loop if vertical 4 in a row found
            break
    if count >= 4:
        return 1
    else:
        return 0
                
### Initialize the game ###

playerkey = {
    True: ['R','Player 1'], 
    False: ['B', 'Player 2']
    } #piece and player dictionary
player1 = False  # turn boolean, needs to default at False
grid = initGrid() # initialize the grid
displayGrid(grid) # print starting grid
gameTurn = 1 #Turn number
connectFour = 0 #Vertical Connect 4
fullGrid = 0

### Play ###

while connectFour == 0 and fullGrid == 0:
    player1 = changePlayer(player1) # ,change players
    print('\n')
    print('Turn',gameTurn,'.',playerkey[player1][1],'please select column to drop piece...')
    input_col = int(input())-1 # user input column
    
    grid = playPiece(grid, input_col, player1, playerkey) # play a piece
    displayGrid(grid) #display new grid
    connectFour = vertCheck(grid, player1, playerkey)  
    fullGrid = fullGridCheck(grid)
    gameTurn += 1

if fullGrid == 1:
    print('Draw! Thanks for playing')
else:
    print(playerkey[player1][1],'wins! Thanks for playing.')