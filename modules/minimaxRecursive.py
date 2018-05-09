# The minimax algorithm which helps select the best move to take
# Nick Conte and Evan Lewis
# Based on pseudocode from AIMA textbook website as stated in part B spec
# http://aima.cs.berkeley.edu/algorithms.pdf

import math
from modules.models import MoveTree


def minimax(moves, stage, board, searchDepth, colourChar):

    MovesTree = MoveTree.MoveTree(moves, stage, board, searchDepth, colourChar)

    root = MovesTree.root

    totalMaxVal = -math.inf
    totalBestMove = None

    for move in root.children:
        value = minVal(move, -math.inf, math.inf)
        if value > totalMaxVal:
            totalMaxVal = value
            totalBestMove = move.move

    return totalBestMove


def maxVal(move, alpha, beta):
    if not move.children:
        return move.value

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
        return move.value

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