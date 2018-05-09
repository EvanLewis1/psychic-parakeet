# Class that represents the move tree and move nodes of Backstab
# Nick Conte and Evan Lewis


from random import *
from copy import deepcopy


from modules import findMoves
from modules.models import Piece
from modules.models.Rules import *
from modules import heuristic



class Node:
    def __init__(self, player, move, board=None, value=None, movenum=0, parent=None):

        # Player making the move
        self.player = player

        # Initial and final position of moved piece
        self.move = move

        # Current board
        self.board = board

        # Value given to move
        self.value = value

        # Count of moves
        self.moveNum = movenum

        # Parent node
        self.parent = parent

        # Children nodes
        self.children = []

        # Best child move
        self.bestChildMove = None

    def printNode(self):
        print("NODE: ")
        print(self.move)


class MoveTree:
    def __init__(self, moves, stage, board, depth, colourChar):

        # Root of the tree
        self.root = None

        self.initiateBuildTree(moves, stage, board, depth, colourChar)

    def initiateBuildTree(self, moves, stage, board, depth, colourChar):
        self.root = Node(colourChar, 0)

        self.root.board = board

        self.buildTree(moves, self.root, stage, self.root.board, depth)

    def buildTree(self, moves, parent, stage, board, depth):

        for move in moves:

            node = Node(Piece.Piece.opposite(parent.player), move, board)

            node.moveNum = parent.moveNum + 1
            node.parent = parent

            node.board = deepcopy(parent.board)
            node.board.applyMove(move, stage, node.player)

            parent.children.append(node)

            if node.moveNum >= depth:
                # Uses heuristic to give value
                node.value = heuristic.heuristic_controlOfCentre(node.board, Piece.Piece.opposite(parent.player))
                return

        for child in parent.children:
            newMoves = findMoves.possibleMoves(child.board, child.player, stage)[0]
            self.buildTree(newMoves, child, stage, child.parent.board, depth)

        return
