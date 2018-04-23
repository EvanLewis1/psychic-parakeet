# Class that represents player of Backstab
# Nick Conte and Evan Lewis


from modules.models.Board2 import Board
from modules import findMoves
from modules.models import Piece

class Player:
    def __init__(self, colour):
        self.PRINTPROCESS = True

        self.colour = colour
        if colour == "white":
            self.colourChar = "O"
            self.PRINTPROCESS = False
        else:
            self.colourChar = "@"

        self.turns = 0
        self.board = Board()
        if self.PRINTPROCESS:
            print("New Board")
            self.board.printBoard()


    def action(self, turns):
        return self.getNextMove()

    def update(self, action):
        placing = self.turns < 24

        if self.PRINTPROCESS:
            print("for turn " + str(self.turns + 1))
            print("Opponent of colour " + Piece.Piece.opposite(self.colourChar))
            print("Plays " + str(action))
            print("Going from ")
            self.board.printBoard()
            print("To")

        self.board.applyMove(action, placing, Piece.Piece.opposite(self.colourChar))

        if self.PRINTPROCESS:
            self.board.printBoard()

        self.turns += 1

    def getNextMove(self):
        if self.PRINTPROCESS:
            print("for turn " + str(self.turns + 1))
            print("I of colour " + self.colourChar)

        placing = self.turns < 24

        move = findMoves.possibleMoves(self.board, self.colourChar, placing)[0][1]

        if self.PRINTPROCESS:
            print("Play " + str(move))
            print("Going from ")
            self.board.printBoard()
            print("To")

        self.board.applyMove(move, placing, self.colourChar)
        if self.PRINTPROCESS:
            self.board.printBoard()
        self.turns += 1

        if(self.colour == "white"):
            self.board.currentState[5][5] = "Wall"

        return move
