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

###########################################################
PIECEWORTH = 10
PIECEINDANGERWORTH = 3

MAXADVANTAGE = PIECEWORTH * 9 + PIECEINDANGERWORTH * 3
MINADVANTAGE = -MAXADVANTAGE

#One player has all 12 pieces, other has 3, all in danger

#Returns chance of winning based on board state
def EvanHeuristic(board, colour):

    #Victory if opponent has two or less pieces
    if len(board.colourPiecesInfo(board.oppcolour(colour))) < 3:
        return MAXADVANTAGE + 1

    #Get piece advantage/disadvantage
    pieceAdvantage = len(board.colourPiecesInfo(board.oppcolour(colour))) - len(board.colourPiecesInfo(colour))

    #Get piece inDanger advantage/disadvantage
    opposingPiecesInDanger = len([piece for piece in board.colourPiecesInfo(board.oppcolour(colour)) if piece.inDanger()])
    piecesInDanger = len([piece for piece in board.colourPiecesInfo(colour) if piece.inDanger()])

    piecesInDangerAdvantage = opposingPiecesInDanger - piecesInDanger

    #Calculate overall advantage
    advantage = pieceAdvantage * PIECEWORTH + piecesInDangerAdvantage * PIECEINDANGERWORTH

    return advantage

