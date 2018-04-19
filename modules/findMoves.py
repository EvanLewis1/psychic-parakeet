from modules.models import board_old


#Prints number of all possible moves for one turn for each colour
def printNumMoves(boardState):
    numMoves, _ = findMoves(boardState)
    print(numMoves)


# Finds all possible moves for one turn for each colour
def findMoves(boardState):
    moves = []
    newmoves, numWhiteMoves = possibleMoves(boardState, board_old.WHITE)
    moves = moves + newmoves
    newmoves, numBlackMoves = possibleMoves(boardState, board_old.BLACK)

    moves = moves + newmoves
    numMoves = str(numWhiteMoves) + "\n" + str(numBlackMoves)
    return numMoves, moves


# Finds all possible moves for one turn for a given colour
def possibleMoves(boardState, colour):
    numMoves = 0
    moves = []
    pieces = board_old.colourPiecesInfo(boardState, colour)

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
    column = piece.pos[1]
    row = piece.pos[0]

    # logic
    # for input piece,

    # for each direction left right up down
    # if one tile in direction is open space add move (1 tile move)
    # else if piece is there and open space one tile furthere is open add a move (Jump move)

    # left
    if column > 0:

        if boardState[row][column - 1] == board_old.EMPTY:
            numMoves = numMoves + 1
            moves.append(((row, column), (row, column - 1)))

        elif boardState[row][column - 1] == board_old.WHITE or boardState[row][column - 1] == board_old.BLACK:
            if column > 1:
                if boardState[row][column - 2] == board_old.EMPTY:
                    moves.append(((row, column), (row, column - 2)))
                    numMoves = numMoves + 1

    # right
    if column < board_old.boardSize - 1:

        if boardState[row][column + 1] == board_old.EMPTY:
            numMoves = numMoves + 1
            moves.append(((row, column), (row, column + 1)))

        elif boardState[row][column + 1] == board_old.WHITE or boardState[row][column + 1] == board_old.BLACK:
            if column < board_old.boardSize - 2:
                if boardState[row][column + 2] == board_old.EMPTY:
                    numMoves = numMoves + 1
                    moves.append(((row, column), (row, column + 2)))
    # up
    if row > 0:

        if boardState[row - 1][column] == board_old.EMPTY:
            numMoves = numMoves + 1
            moves.append(((row, column), (row - 1, column)))

        elif boardState[row - 1][column] == board_old.WHITE or boardState[row - 1][column] == board_old.BLACK:
            if row > 1:
                if boardState[row - 2][column] == board_old.EMPTY:
                    numMoves = numMoves + 1
                    moves.append(((row, column), (row - 2, column)))

    # down
    if row < board_old.boardSize - 1:

        if boardState[row + 1][column] == board_old.EMPTY:
            numMoves = numMoves + 1
            moves.append(((row, column), (row + 1, column)))

        elif boardState[row + 1][column] == board_old.WHITE or boardState[row + 1][column] == board_old.BLACK:
            if row < board_old.boardSize - 2:
                if boardState[row + 2][column] == board_old.EMPTY:
                    numMoves = numMoves + 1
                    moves.append(((row, column), (row + 2, column)))

    return moves, numMoves
