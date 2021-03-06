# Used to model the board of the game "backstab"

# Used for part b

from modules.models.Piece import Piece
from modules.models.Rules import *


class Board:

    def __init__(self, board = False):

        if board:
            self.currentState = []

            for x in range(0, boardSize):
                row = []
                for y in range(0, boardSize):

                    row.append(board[x][y])
                self.currentState.append(row)


            for x in range(0, boardSize):
                for y in range(0, boardSize):
                    if self.currentState[x][y] != board[x][y]:
                        print("ERROR not same")
                        exit(0)

        else:
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

    def applyMove(self, move, stage=MOVE1, colour=None):

        # If forfeit
        if move is None:
            return

        # If in placing stage put piece at move's location
        if stage == PLACING:
            self.currentState[move[0]][move[1]] = colour

        # Else move a piece on the board
        else:
            # Get piece's colour
            colour = self.currentState[move[0][0]][move[0][1]]
            if colour == EMPTY:
                print("Error move is incorrect")
                exit(0)

            # Remove piece from original position
            self.currentState[move[0][0]][move[0][1]] = EMPTY

            # Add piece to destination
            self.currentState[move[1][0]][move[1][1]] = colour

        # Remove dead pieces
        self.wipeDeadPieces(colour)

    def wipeDeadPieces(self, whosTurn, ignoreColour=False):

        # For all pieces of current colour
        for focusColour in [Piece.opposite(whosTurn), whosTurn]:  # Wipe opposing pieces (Before current turn's pieces)
            for column in range(0, boardSize):
                for row in range(0, boardSize):

                    checkPiece = False
                    if self.currentState[column][row] == focusColour:
                        checkPiece = True
                        colour = focusColour

                    if self.currentState[column][row] == Piece.opposite(focusColour) and ignoreColour:
                        checkPiece = True
                        colour = Piece.opposite(focusColour)


                    if checkPiece:

                        # If surrounded vertically
                        if 0 < row < boardSize - 1:
                            if (self.currentState[column][row - 1] == Piece.opposite(colour) or self.currentState[
                                column][row - 1] == CORNER) \
                                    and (
                                    self.currentState[column][row + 1] == Piece.opposite(colour) or self.currentState[
                                        column][row + 1] == CORNER):

                                # Remove
                                self.currentState[column][row] = EMPTY

                        # if surrounded horizontally
                        if 0 < column < boardSize - 1:
                            if (self.currentState[column - 1][row] == Piece.opposite(colour) or (
                                    self.currentState[column - 1][row] == CORNER)) \
                                    and (
                                    self.currentState[column + 1][row] == Piece.opposite(colour) or self.currentState[
                                        column + 1][row] == CORNER):

                                # Remove
                                self.currentState[column][row] = EMPTY

    def shrink(self, amount):
        border = amount - 1

        # Change outer tiles to out of bounds '!'
        for column in range(0, boardSize):
            for row in range(0, boardSize):
                if row == border or row == boardSize - border - 1 or column == border or column == boardSize - border - 1:

                    self.currentState[column][row] = OUTOFBOUNDS

        # Create new corners


        #Wipe Pieces
        self.currentState[amount][boardSize - amount-1] = EMPTY
        self.currentState[amount][amount] = EMPTY
        self.currentState[boardSize - amount -1][boardSize - amount -1] = EMPTY
        self.currentState[boardSize - amount -1][amount] = EMPTY


        # TopLeft
        self.currentState[amount][amount] = CORNER
        self.wipeDeadPieces(WHITE, True)
        # BottomLeft
        self.currentState[amount][boardSize - amount-1] = CORNER
        self.wipeDeadPieces(WHITE, True)
        # BottomRight
        self.currentState[boardSize - amount -1][boardSize - amount -1] = CORNER
        self.wipeDeadPieces(WHITE, True)
        # TopRight
        self.currentState[boardSize - amount -1][amount] = CORNER
        self.wipeDeadPieces(WHITE, True)
