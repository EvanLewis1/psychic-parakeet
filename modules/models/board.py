#Used to model the board of the game "backstab"

BLACK = "@"
WHITE = "O"
EMPTY = "-"
CORNER = "X"

boardSize = 8

class piece:
    def __init__(self, colour, pos, touchingOpposingPiece = False):
        self.touchingOpposingPiece = touchingOpposingPiece
        self.pos = pos
        self.colour = colour

def blackPiecesExist(boardState):
    for row in boardState:
        for tile in row:
            if tile == BLACK:
                return True
    return False

def colourPiecesInfo(boardState, colour):

    pieces = []
    for row in range(0,boardSize):
        for column in range(0,boardSize):
            if boardState[row][column] == colour:
                colourPiece = piece(colour, (row,column))
                pieces.append(colourPiece)

    return pieces


def opposite(colour):
    if colour == WHITE:
        return BLACK
    elif colour == BLACK:
        return WHITE
    else:
        print("error: \'" + str(colour) + "\' not colour")

