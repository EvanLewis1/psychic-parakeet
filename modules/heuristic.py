from modules.models.Rules import *
from random import *


# Creates a value for a given board state
def heuristic(oldBoard, newBoard):

    # Removing a piece is given a very high value, losing a piece is given a very low value
    #takenPiecesVal = ((len(oldBoard.colourPiecesInfo(BLACK)) - len(newBoard.colourPiecesInfo(BLACK))) -
                     # (len(oldBoard.colourPiecesInfo(WHITE)) - len(newBoard.colourPiecesInfo(WHITE)))) * 10

    takenPiecesVal = (len(oldBoard.colourPiecesInfo(BLACK)) - len(newBoard.colourPiecesInfo(BLACK))) * 10

    # The number of adjacent pieces (pieces in danger)
    dangerVal = 0

    for piece in newBoard.colourPiecesInfo(BLACK):
        if piece.inDanger(newBoard.currentState):
            dangerVal += 3

    # Random int to prevent repeating unhelpful moves
    randVal = randint(1, 2)

    # Final value combines all elements
    value = takenPiecesVal + randVal + dangerVal
    return value