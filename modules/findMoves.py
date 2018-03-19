BLACK = "@"
WHITE = "O"
EMPTY = "-"
CORNER = "X"

boardSize = 8

def printNumMoves(boardState):
    numMoves, _ = findMoves(boardState)
    print(numMoves)

def findMoves(boardState):
    moves = []
    numMoves = ""
    newmoves, numWhiteMoves = possibleMoves(boardState, WHITE)
    moves = moves + newmoves
    newmoves, numBlackMoves = possibleMoves(boardState, BLACK)

    moves = moves + newmoves
    numMoves = str(numWhiteMoves) + "\n" + str(numBlackMoves)
    return numMoves, moves


def possibleMoves(boardState, colour):
    numMoves = 0
    moves = []


    #logic
    #for each piece of the input colour,


    for row in range(0, boardSize):
        for column in range(0, boardSize):
            if (boardState[row][column] == colour):

                # for each direction left right up down
                # if one tile in direction is open space +1
                # else if piece is there and open space one tile furthere is open +1


                #left
                if column > 0:
                    if boardState[row][column-1] == EMPTY:
                        numMoves = numMoves + 1
                        moves.append(((row,column),(row,column-1)))
                    elif boardState[row][column-1] == WHITE or boardState[row][column-1] == BLACK:
                        if column > 1:
                            if boardState[row][column-2] == EMPTY:
                                moves.append(((row,column), (row, column-2)))
                                numMoves = numMoves + 1

                #right
                if column < boardSize-1:
                    if boardState[row][column + 1] == EMPTY:
                        numMoves = numMoves + 1
                        moves.append(((row,column), (row,column+1)))
                    elif boardState[row][column + 1] == WHITE or boardState[row][column + 1] == BLACK:
                        if column < boardSize-2:
                            if boardState[row][column + 2] == EMPTY:
                                numMoves = numMoves + 1
                                moves.append(((row,column), (row, column+2)))
                #up
                if row > 0:
                    if  boardState[row-1][column] == EMPTY:
                        numMoves = numMoves + 1
                        moves.append(((row,column),(row-1, column)))
                    elif boardState[row-1][column] == WHITE or boardState[row-1][column] == BLACK:
                        if row > 1:
                            if  boardState[row-2][column] == EMPTY:
                                numMoves = numMoves + 1
                                moves.append(((row, column), (row - 2, column)))

                #down
                if row < boardSize-1:
                    if  boardState[row+1][column] == EMPTY:
                        numMoves = numMoves + 1
                        moves.append(((row,column),(row+1, column)))

                    elif boardState[row+1][column] == WHITE or boardState[row+1][column] == BLACK:
                        if row < boardSize-2:
                            if  boardState[row+2][column] == EMPTY:
                                numMoves = numMoves + 1
                                moves.append(((row, column), (row + 2, column)))

    return moves, numMoves
