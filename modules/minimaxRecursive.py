# The minimax algorithm which helps select the best move to take
# Nick Conte and Evan Lewis
# Based on pseudocode from AIMA textbook website as stated in part B spec
# http://aima.cs.berkeley.edu/algorithms.pdf

PRINTPROCESS = False

import math
from modules.models import MoveTree

from modules.heuristic import heuristic_controlOfCentre

#Chooses best move
def minimax(moves, stage, board, searchDepth, colourChar):

    #Create Move Tree
    print("start")
    MovesTree = MoveTree.MoveTree(moves, stage, board, searchDepth, colourChar)
    print("end")

    root = MovesTree.root


    totalMaxVal = -math.inf
    totalBestMove = None

    #Find best move
    for move in root.children:
        value = minVal(move, -math.inf, math.inf)

        if PRINTPROCESS:
            move.board.printBoard()
            print("Supposed value: " + str(value))
            print("value: " + str(heuristic_controlOfCentre(move)))
            print("for: " + colourChar)

        if value > totalMaxVal:
            totalMaxVal = value
            totalBestMove = move.move
            if PRINTPROCESS:
                move.board.printBoard()
                print("value: " + str(heuristic_controlOfCentre(move)))
                print("for: " + colourChar)
    #Return best move
    return totalBestMove


def maxVal(move, alpha, beta):
    if not move.children:
        return heuristic_controlOfCentre(move)

    maxVal = -math.inf

    for move in move.children:
        minMoveVal = minVal(move, alpha, beta)
        if minMoveVal > maxVal:
            maxVal = minMoveVal
        if maxVal >= beta:
            return maxVal
        if maxVal > alpha:
            alpha = maxVal

    return maxVal


def minVal(move, alpha, beta):
    if not move.children:
        return heuristic_controlOfCentre(move)

    minVal = math.inf

    for move in move.children:
        maxMoveVal = maxVal(move, alpha, beta)
        if maxMoveVal < minVal:
            minVal = maxMoveVal
        if minVal <= alpha:
            return minVal
        if minVal < beta:
            beta = minVal

    return minVal