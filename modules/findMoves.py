from modules.models import Board2
from modules.models.Rules import *


#Prints number of all possible moves for one turn for each colour
def printNumMoves(boardState):
    numMoves, _ = findMoves(boardState)
    print(numMoves)


# Finds all possible moves for one turn for each colour
def findMoves(boardState):
    moves = []
    newmoves, numWhiteMoves = possibleMoves(boardState, Board2.WHITE)
    moves = moves + newmoves
    newmoves, numBlackMoves = possibleMoves(boardState, Board2.BLACK)

    moves = moves + newmoves
    numMoves = str(numWhiteMoves) + "\n" + str(numBlackMoves)
    return numMoves, moves


# Finds all possible moves for one turn for a given colour
def possibleMoves(board, colour, stage = MOVE1):
    boardState = board.currentState

    numMoves = 0
    moves = []

    if stage == PLACING:

        if colour == Board2.WHITE:
            zoneStart = 0
            zoneEnd = Board2.boardSize -2
        else:
            zoneStart = 2
            zoneEnd = Board2.boardSize

        for row in range(zoneStart, zoneEnd):
            for column in range(0, Board2.boardSize):
                if boardState[column][row] == Board2.EMPTY:
                    numMoves +=1
                    moves.append((column, row))

    else:
        pieces = board.colourPiecesInfo(colour)

        # logic
        # for each piece of the input colour,

        for piece in pieces:
            pieceMoves, numPieceMoves = onePiecePossibleMoves(boardState, piece)
            numMoves += numPieceMoves
            moves += pieceMoves
    return moves, numMoves

# Finds all possible moves for one turn for a given piece
def onePiecePossibleMoves(boardState, piece):
    numMoves = 0
    moves = []
    column = piece.pos[0]
    row = piece.pos[1]

    # logic
    # for input piece,

    # for each direction left right up down
    # if one tile in direction is open space add move (1 tile move)
    # else if piece is there and open space one tile furthere is open add a move (Jump move)

    # up
    if row > 0:

        if boardState[column][row - 1] == Board2.EMPTY:
            numMoves = numMoves + 1
            moves.append(((column, row), (column, row - 1)))

        elif boardState[column][row - 1] == Board2.WHITE or boardState[column][row - 1] == Board2.BLACK:
            if row > 1:
                if boardState[column][row - 2] == Board2.EMPTY:
                    moves.append(((column, row), (column, row - 2)))
                    numMoves = numMoves + 1

    # down
    if row < Board2.boardSize - 1:

        if boardState[column][row + 1] == Board2.EMPTY:
            numMoves = numMoves + 1
            moves.append(((column, row), (column, row + 1)))

        elif boardState[column][row + 1] == Board2.WHITE or boardState[column][row + 1] == Board2.BLACK:
            if row < Board2.boardSize - 2:
                if boardState[column][row + 2] == Board2.EMPTY:
                    numMoves = numMoves + 1
                    moves.append(((column, row), (column, row + 2)))
    # left
    if column > 0:

        if boardState[column - 1][row] == Board2.EMPTY:
            numMoves = numMoves + 1
            moves.append(((column, row), (column - 1, row)))

        elif boardState[column - 1][row] == Board2.WHITE or boardState[column - 1][row] == Board2.BLACK:
            if column > 1:
                if boardState[column - 2][row] == Board2.EMPTY:
                    numMoves = numMoves + 1
                    moves.append(((column, row), (column - 2, row)))

    # right
    if column < Board2.boardSize - 1:

        if boardState[column + 1][row] == Board2.EMPTY:
            numMoves = numMoves + 1
            moves.append(((column, row), (column + 1, row)))

        elif boardState[column + 1][row] == Board2.WHITE or boardState[column + 1][row] == Board2.BLACK:
            if column < Board2.boardSize - 2:
                if boardState[column + 2][row] == Board2.EMPTY:
                    numMoves = numMoves + 1
                    moves.append(((column, row), (column + 2, row)))

    return moves, numMoves
