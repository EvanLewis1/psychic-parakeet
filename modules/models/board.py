#Used to model the board of the game "backstab"

BLACK = "@"
WHITE = "O"
EMPTY = "-"
CORNER = "X"

boardSize = 8

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3



class piece:
    def __init__(self, colour, pos, touchingOpposingPiece = False, adjacentTiles = [False,False,False,False]):
        self.pos = pos
        self.colour = colour
        self.touchingOpposingPiece = touchingOpposingPiece
        self.adjacentTiles = adjacentTiles


    def adjacent(self, pos):
        if (abs(self.pos[0] - pos[0]) == 1 and abs(self.pos[1] - pos[1]) == 0) or (abs(self.pos[1] - pos[1]) == 1 and abs(self.pos[0] - pos[0]) == 0):
            return True
        return False
    
    def isLethal(self, pos):
        if self.pos[0] - pos[0] == 1 and self.pos[1] - pos[1] == 0:
            return self.adjacentTiles[DOWN]

        if self.pos[0] - pos[0] == -1 and self.pos[1] - pos[1] == 0:
            return self.adjacentTiles[UP]

        if self.pos[0] - pos[0] == 0 and self.pos[1] - pos[1] == 1:
            return self.adjacentTiles[RIGHT]

        if self.pos[0] - pos[0] == 0 and self.pos[1] - pos[1] == -1:
            return self.adjacentTiles[LEFT]

        print("Error: not adjacent")
        return False




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

                touchingOpposingPiece = False
                adjacentTiles = [False,False,False,False]
                if (row < boardSize):
                    if boardState[row + 1][column] == opposite(colour):
                        touchingOpposingPiece = True
                        adjacentTiles[DOWN] = True
                if (row > 0):
                    if boardState[row - 1] [column] == opposite(colour):
                        touchingOpposingPiece = True
                        adjacentTiles[UP] = True

                if (column < boardSize):
                    if boardState[row][ column + 1] == opposite(colour):
                        touchingOpposingPiece = True
                        adjacentTiles[RIGHT] = True

                if (column > 0):
                    if boardState[row] [column - 1] == opposite(colour):
                        touchingOpposingPiece = True
                        adjacentTiles[LEFT] = True


                colourPiece = piece(colour, (row,column), touchingOpposingPiece, adjacentTiles)
                pieces.append(colourPiece)

    return pieces


def opposite(colour):
    if colour == WHITE:
        return BLACK
    elif colour == BLACK:
        return WHITE
    else:
        print("error: \'" + str(colour) + "\' not colour")

def printBoardState(boardState):
    for row in boardState:
        line = ""
        for tile in row:
            line = line + tile + " "
        print(line)
