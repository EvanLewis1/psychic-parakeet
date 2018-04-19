# Class that represents player of Backstab
# Nick Conte and Evan Lewis

from modules.models import Board2
from modules import findMoves

class Player:
    def __init__(self, colour):
        self.colour = colour
        self.turns = 0
        self.board = Board2()

    def action(self, turns):
        return self.getNextMove()

    def update(self, action):
        self.board.applyMove(action)

    def getNextMove(self):

        return None
