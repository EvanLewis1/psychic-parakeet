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

    while(board.blackPiecesExist(currentBoardState)):
        # Logic for next move
        nextMove = findNextMove(currentBoardState)

        massacreMoves.append(nextMove)

        currentBoardState = applyMove(nextMove, currentBoardState)

        # continue loop

    return massacreMoves


def findNextMove(boardState):
    nextMove = ()

    numMoves, possibleMoves = findMoves.findMoves(boardState)
    targetPieces = board.colourPiecesInfo(boardState, board.BLACK)

    # Find black piece to target
    targetPiece = targetPieces[0]
    for piece in targetPieces:
        if piece.touchingOpposingPiece:
            targetPiece = piece

    # Find closest white piece to use against target piece

    # Search for path from white piece to black piece

    # return first step in path

    return nextMove

def applyMove(move, boardState):

    newBoardState = boardState[:] #copy list

    # Get piece's colour
    colour = boardState[move[0][0], move[0][1]]

    # Remove piece from original position
    newBoardState[move[0][0], move[0][1]] = board.EMPTY

    # Add piece to destination
    newBoardState[move[1][0], move[1][1]] = colour

    newBoardState = wipeDeadPieces(newBoardState, colour)

    return newBoardState

def wipeDeadPieces(boardState, whosTurn):

    #Wipe opposing pieces (Before current turn's pieces!)
    for row in range(0,board.boardSize):
        for column in range(0,board.boardSize):
            if boardState[row][column] == board.opposite(whosTurn):
                #if surrounded
                if(False):
                    boardState[row][column] = board.EMPTY

    #Wipe current turn's pieces
    for row in range(0,board.boardSize):
        for column in range(0,board.boardSize):
            if boardState[row][column] == whosTurn:
                #if surrounded
                if(False):
                    boardState[row][column] = board.EMPTY


    return boardState


