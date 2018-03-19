import modules.parse as parse
import modules.findMoves as findMoves
import modules.findPath as findPath

MOVES = 'Moves'

#Main file for part a
#Takes in text representing board state and option (Possible moves or path to victory)
#Returns answer to option based on board state

#read input (parse.py (parseInput()))
(boardState, option)= parse.parse()

#if line 9 is find moves (parse.py (parse.input))
#calculate moves (findMoves.py (findMoves()))
if (option == MOVES):
    findMoves.findMoves(boardState)
#Else
else:
    findPath.findPath(boardState)
#Find path (findPath.py (findPath()))