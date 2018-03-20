#Main file for part a
#Takes in text representing board state and option (Possible moves or path to victory)
#prints answer to option based on board state

#Nick Conte
#Evan Lewis

import modules.parse as parse
import modules.findMoves as findMoves
import modules.findPath as findPath

MOVES = 'Moves'
MASSACRE = 'Massacre'


#read input
(boardState, option)= parse.parse()

#if line 9 is find moves (parse.py (parse.input))
if (option == MOVES):
    findMoves.printNumMoves(boardState)
#Else print path to victory for white
else:
    findPath.printMassacrePath(boardState)
