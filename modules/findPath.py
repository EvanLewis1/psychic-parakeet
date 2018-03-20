import modules.findMoves as findMoves
from modules.models import  board


def printMassacrePath(boardState):
    path = findPath(boardState)
    pathString = ""
    for move in path:
        pathString = pathString + str(move)

    print(pathString)


def findPath(boardState):

    currentBoardState = boardState

    massacreMoves = []

    while(board.blackPiecesExist(boardState)):
        numMoves, possibleMoves = findMoves.findMoves(currentBoardState)

        # Logic for next move

        # massacreMoves.append(next move)

        # currentBoardState = applyMove(next move, currentBoardState)

        # end loop

    return massacreMoves


