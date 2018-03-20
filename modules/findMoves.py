from modules.models import board


def printNumMoves(boardState):
    numMoves, _ = findMoves(boardState)
    print(numMoves)


def findMoves(boardState):
    moves = []
    numMoves = ""
    newmoves, numWhiteMoves = possibleMoves(boardState, board.WHITE)
    moves = moves + newmoves
    newmoves, numBlackMoves = possibleMoves(boardState, board.BLACK)

    moves = moves + newmoves
    numMoves = str(numWhiteMoves) + "\n" + str(numBlackMoves)
    return numMoves, moves


def possibleMoves(boardState, colour):
    numMoves = 0
    moves = []

    # logic
    # for each piece of the input colour,

    for row in range(0, board.boardSize):
        for column in range(0, board.boardSize):
            if (boardState[row][column] == colour):

                # for each direction left right up down
                # if one tile in direction is open space +1
                # else if piece is there and open space one tile furthere is open +1

                # left
                if column > 0:

                    if boardState[row][column - 1] == board.EMPTY:
                        numMoves = numMoves + 1
                        moves.append(((row, column), (row, column - 1)))

                    elif boardState[row][column - 1] == board.WHITE or boardState[row][column - 1] == board.BLACK:
                        if column > 1:
                            if boardState[row][column - 2] == board.EMPTY:
                                moves.append(((row, column), (row, column - 2)))
                                numMoves = numMoves + 1

                # right
                if column < board.boardSize - 1:

                    if boardState[row][column + 1] == board.EMPTY:
                        numMoves = numMoves + 1
                        moves.append(((row, column), (row, column + 1)))

                    elif boardState[row][column + 1] == board.WHITE or boardState[row][column + 1] == board.BLACK:
                        if column < board.boardSize - 2:
                            if boardState[row][column + 2] == board.EMPTY:
                                numMoves = numMoves + 1
                                moves.append(((row, column), (row, column + 2)))
                # up
                if row > 0:

                    if boardState[row - 1][column] == board.EMPTY:
                        numMoves = numMoves + 1
                        moves.append(((row, column), (row - 1, column)))

                    elif boardState[row - 1][column] == board.WHITE or boardState[row - 1][column] == board.BLACK:
                        if row > 1:
                            if boardState[row - 2][column] == board.EMPTY:
                                numMoves = numMoves + 1
                                moves.append(((row, column), (row - 2, column)))

                # down
                if row < board.boardSize - 1:

                    if boardState[row + 1][column] == board.EMPTY:
                        numMoves = numMoves + 1
                        moves.append(((row, column), (row + 1, column)))

                    elif boardState[row + 1][column] == board.WHITE or boardState[row + 1][column] == board.BLACK:
                        if row < board.boardSize - 2:
                            if boardState[row + 2][column] == board.EMPTY:
                                numMoves = numMoves + 1
                                moves.append(((row, column), (row + 2, column)))

    return moves, numMoves
