BLACK = "@"
WHITE = "O"
EMPTY = "-"
CORNER = "X"

boardSize = 8

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Piece:
    # Class for a piece on the board
    def __init__(self, colour, pos):
        self.pos = pos
        self.colour = colour
        # self.touchingOpposingPiece = touchingOpposingPiece
        # self.adjacentTiles = adjacentTiles

    @staticmethod
    def opposite(colour):
        if colour == WHITE:
            return BLACK
        elif colour == BLACK:
            return WHITE
        else:
            print("error: \'" + str(colour) + "\' not colour")
            exit(0)

    # Return true if given piece is adjacent to this piece
    def adjacent(self, pos):
        if (abs(self.pos[0] - pos[0]) == 1 and abs(self.pos[1] - pos[1]) == 0) or (abs(self.pos[1] - pos[1]) == 1 and abs(self.pos[0] - pos[0]) == 0):
            return True
        return False

    # Return true if this piece is next to opposing piece or corner
    def inDanger(self, boardState):
        row = self.pos[0]
        column = self.pos[1]
        if (row < boardSize - 1):
            if boardState[row + 1][column] == self.opposite(self.colour) or boardState[row + 1][column] == CORNER:
                return True
        if (row > 0):
            if boardState[row - 1][column] == self.opposite(self.colour) or boardState[row - 1][column] == CORNER:
                return  True

        if (column < boardSize - 1):
            if boardState[row][column + 1] == self.opposite(self.colour) or boardState[row][column + 1] == CORNER:
                return  True

        if (column > 0):
            if boardState[row][column - 1] == self.opposite(self.colour) or boardState[row][column - 1] == CORNER:
                return  True
        return False

    # Return array of bools representing where corners/opposing pieces are
    def adjacentTiles(self, boardState):
        row = self.pos[0]
        column = self.pos[1]

        adjacentTiles = [False,False,False,False]
        if (row < boardSize - 1):
            if boardState[row + 1][column] == self.opposite(self.colour) or boardState[row + 1][column] == CORNER:
                adjacentTiles[DOWN] = True
        if (row > 0):
            if boardState[row - 1][column] == self.opposite(self.colour) or boardState[row - 1][column] == CORNER:
                adjacentTiles[UP] = True

        if (column < boardSize - 1):
            if boardState[row][column + 1] == self.opposite(self.colour) or boardState[row][column + 1] == CORNER:
                adjacentTiles[RIGHT] = True

        if (column > 0):
            if boardState[row][column - 1] == self.opposite(self.colour) or boardState[row][column - 1] == CORNER:
                adjacentTiles[LEFT] = True

        return adjacentTiles

    # Return true if an opposing piece placed in pos would kill this piece
    def isLethal(self, pos, boardState):
        if self.pos[0] - pos[0] == 1 and self.pos[1] - pos[1] == 0:
            return self.adjacentTiles(boardState)[DOWN]

        if self.pos[0] - pos[0] == -1 and self.pos[1] - pos[1] == 0:
            return self.adjacentTiles(boardState)[UP]

        if self.pos[0] - pos[0] == 0 and self.pos[1] - pos[1] == 1:
            return self.adjacentTiles(boardState)[RIGHT]

        if self.pos[0] - pos[0] == 0 and self.pos[1] - pos[1] == -1:
            return self.adjacentTiles(boardState)[LEFT]

        print("Error: not adjacent")
        return False

    def distFromCentre(self):
        columnDist = min(abs(self.pos[0]-3), abs(self.pos[0]-4))
        rowDist    = min(abs(self.pos[1]-3), abs(self.pos[1]-4))

        return rowDist + columnDist

