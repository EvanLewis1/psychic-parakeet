from modules.models.Rules import *
from modules.models import Piece



PIECEWORTH = 10

#Returns the advantage(as a number/score) that the given colour has, can be negative to represent a disadvantage
def heuristic_controlOfCentre(move):

    board = move.board
    colour = move.player
    stage = move.stage
    depth = move.moveNum

    if depth%2 ==0:
        colour = Piece.Piece.opposite(colour)

    #Victory if opponent has two or less pieces
    if len(board.colourPiecesInfo(Piece.Piece.opposite(colour))) < 3 and stage > PLACING:
        return 1000

    # Loss if  has two or less pieces
    if len(board.colourPiecesInfo(colour)) < 3 and stage > PLACING:
        return -1000


    #Strength of my pieces
    myBoardPower = 0
    myPieces = board.colourPiecesInfo(colour)

    for myPiece in myPieces:
        myBoardPower += PIECEWORTH - myPiece.distFromCentre()

    #Strength of opponents pieces
    oppBoardPower = 0
    oppPieces = board.colourPiecesInfo(Piece.Piece.opposite(colour))
    for oppPiece in oppPieces:
        oppBoardPower += PIECEWORTH - oppPiece.distFromCentre()


    advantage = myBoardPower - oppBoardPower
    # print(advantage)
    return advantage
