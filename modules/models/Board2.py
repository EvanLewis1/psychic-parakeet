#Used to model the board of the game "backstab"

# Used for part b

from modules.models import Piece

BLACK = "@"
WHITE = "O"
EMPTY = "-"
CORNER = "X"

boardSize = 8

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

STARTINGSTATE = []
for x in range(0, boardSize):
    row = []
    for y in range(0, boardSize):
        row.append(EMPTY)
    STARTINGSTATE.append(row)

STARTINGSTATE[0][boardSize-1] = CORNER
STARTINGSTATE[0][boardSize-1] = CORNER
STARTINGSTATE[boardSize-1][0] = CORNER
STARTINGSTATE[boardSize-1][0] = CORNER


class Board:

    def __init__(self, state=STARTINGSTATE):
        self.currentState = state

    def blackPiecesExist(self):
        for row in self.currentState:
            for tile in row:
                if tile == BLACK:
                    return True
        return False


    # Return all list of all pieces of given colour
    def colourPiecesInfo(self, colour):
        pieces = []
        for row in range(0, boardSize):
            for column in range(0, boardSize):
                if self.currentState[row][column] == colour:
                    colourPiece = Piece(colour, (row,column))
                    pieces.append(colourPiece)

        return pieces

    def printBoard(self):
        for row in self.currentState:
            line = ""
            for tile in row:
                line = line + tile + " "
            print(line)

    def applyMove(self, move):

        # Get piece's colour
        colour = self.currentState[move[0][0]][move[0][1]]
        # Remove piece from original position
        self.currentState[move[0][0]][move[0][1]] = self.currentState.EMPTY

        # Add piece to destination
        self.currentState[move[1][0]][move[1][1]] = colour

        # Remove dead pieces
        self.wipeDeadPieces(self.currentState, colour)

    def wipeDeadPieces(self, whosTurn):
        # Wipe opposing pieces (Before current turn's pieces!)
        for colour in [Piece.Piece.opposite(whosTurn), whosTurn]:
            for row in range(0, boardSize):
                for column in range(0, boardSize):
                    if self.currentState[row][column] == colour:
                        # if surrounded vertically
                        if 0 < row < boardSize - 1:
                            if (self.currentState[row - 1][column] == Piece.opposite(colour) or self.currentState[row - 1][
                                column] == CORNER) \
                                    and (self.currentState[row + 1][column] == Piece.opposite(colour) or self.currentState[row + 1][
                                column] == CORNER):
                                self.currentState[row][column] = EMPTY  # Remove

                        # if surrounded horizontally
                        if 0 < column < boardSize - 1:
                            if (self.currentState[row][column - 1] == Piece.opposite(colour) or (
                                    self.currentState[row][column - 1] == CORNER)) \
                                    and (self.currentState[row][column + 1] == Piece.opposite(colour) or self.currentState[row][
                                column + 1] == CORNER):
                                self.currentState[row][column] = EMPTY  # Remove
