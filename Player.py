# Class that represents player of Backstab
# Nick Conte and Evan Lewis

import random


from modules.models.Board2 import Board
from modules import findMoves
from modules.models import Piece
from modules.models.Rules import *


class Player:
    def __init__(self, colour):

        #Print the thought process of program
        self.PRINTPROCESS = True

        #Playing colour
        self.colour = colour

        #single character representation of colour
        if colour == "white":
            self.colourChar = "O"
        else:
            self.colourChar = "@"

        self.turns = 0
        self.stage = PLACING
        self.board = Board()

        if self.PRINTPROCESS:
            print("New Board")
            self.board.printBoard()

    def action(self, turns):
        return self.getNextMove()

    def update(self, action):

        if self.PRINTPROCESS:
            print("for turn " + str(self.turns + 1))
            print("Opponent of colour " + Piece.Piece.opposite(self.colourChar))
            print("Plays " + str(action))
            print("Going from ")
            self.board.printBoard()
            print("To")

        # Apply opponent's move to board representation
        self.board.applyMove(action, self.stage, Piece.Piece.opposite(self.colourChar))

        if self.PRINTPROCESS:
            self.board.printBoard()

        # Count the turn
        self.nextTurn()

    def getNextMove(self):
        if self.PRINTPROCESS:
            print("for turn " + str(self.turns + 1))
            print("I of colour " + self.colourChar)

        #Get all possible moves
        possibleMoves, numMoves = findMoves.possibleMoves(self.board, self.colourChar, self.stage)

        if numMoves > 0:
            move = possibleMoves[random.randrange(0, numMoves)]
        else:
            move = None

        if self.PRINTPROCESS:
            print("Have " + str(numMoves) + " possible moves")
            print("Play " + str(move))
            print("Going from ")
            self.board.printBoard()
            print("To")

        # Apply move to board representation
        self.board.applyMove(move, self.stage, self.colourChar)
        if self.PRINTPROCESS:
            self.board.printBoard()

        # Count the turn
        self.nextTurn()

        return move

    def nextTurn(self):
        self.turns += 1

        # Check to see if stage has changed
        if self.turns == STARTMOVE1:
            self.stage = MOVE1
        if self.turns == STARTMOVE2:
            self.board.shrink(1)  # Shrink board
            self.stage = MOVE2
        if self.turns == STARTMOVE3:
            self.board.shrink(2)  # Shrink board
            self.stage = MOVE3


