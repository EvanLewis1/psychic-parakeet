#Used to model the board of the game "backstab"

# Used for part b

from modules.models.Piece import Piece

BLACK = "@"
WHITE = "O"
EMPTY = "-"
CORNER = "X"

boardSize = 8

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Board:

    def __init__(self):

        self.newBoard()

    def newBoard(self):
        STARTINGSTATE = []
        for x in range(0, boardSize):
            row = []
            for y in range(0, boardSize):
                row.append(EMPTY)
            STARTINGSTATE.append(row)

        STARTINGSTATE[0][0] = CORNER
        STARTINGSTATE[0][boardSize - 1] = CORNER
        STARTINGSTATE[boardSize - 1][0] = CORNER
        STARTINGSTATE[boardSize - 1][boardSize - 1] = CORNER
        self.currentState = STARTINGSTATE

    def blackPiecesExist(self):
        for column in self.currentState:
            for tile in column:
                if tile == BLACK:
                    return True
        return False


    # Return all list of all pieces of given colour
    def colourPiecesInfo(self, colour):
        pieces = []
        for column in range(0, boardSize):
            for row in range(0, boardSize):
                if self.currentState[column][row] == colour:
                    colourPiece = Piece(colour, (column, row))
                    pieces.append(colourPiece)

        return pieces

    def printBoard(self):
        for row in range(0, boardSize):
            line = ""
            for column in range(0, boardSize):
                line = line + self.currentState[column][row] + " "
            print(line)

    def applyMove(self, move, placing=False, colour=None):

        if placing:
            print("apply")
            self.currentState[move[0]][move[1]] = colour

        else:
            # Get piece's colour
            colour = self.currentState[move[0][0]][move[0][1]]
            print(move)
            print("colour")
            print(colour)
            # Remove piece from original position
            self.currentState[move[0][0]][move[0][1]] = EMPTY

            # Add piece to destination
            self.currentState[move[1][0]][move[1][1]] = colour

        # Remove dead pieces
        self.wipeDeadPieces(colour)

    def wipeDeadPieces(self, whosTurn):
        # Wipe opposing pieces (Before current turn's pieces!)
        for colour in [Piece.opposite(whosTurn), whosTurn]:
            for column in range(0, boardSize):
                for row in range(0, boardSize):
                    if self.currentState[column][row] == colour:
                        # if surrounded vertically
                        if 0 < row < boardSize - 1:
                            if (self.currentState[column][row - 1] == Piece.opposite(colour) or self.currentState[
                                column][row - 1] == CORNER) \
                                    and (self.currentState[column][row + 1] == Piece.opposite(colour) or self.currentState[
                                column][row + 1] == CORNER):
                                self.currentState[column][row] = EMPTY  # Remove

                        # if surrounded horizontally
                        if 0 < column < boardSize - 1:
                            if (self.currentState[column - 1][row] == Piece.opposite(colour) or (
                                    self.currentState[column - 1][row] == CORNER)) \
                                    and (self.currentState[column + 1][row] == Piece.opposite(colour) or self.currentState[
                                column + 1][row] == CORNER):
                                self.currentState[column][row] = EMPTY  # Remove
