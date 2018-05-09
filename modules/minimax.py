# The minimax algorithm which helps select the best move to take
# Nick Conte and Evan Lewis


from modules.models.Rules import *
from modules.models import MoveTree

def initMinimax(moves, stage, board, depth):

    MovesTree = MoveTree.MoveTree(moves, stage, board, depth)

    nodes = MovesTree.root.children

    while MovesTree.root.value is None:
        minimax(nodes)

    bestMove = MovesTree.root.bestChildMove
    return bestMove


def minimax(nodes):
    for node in nodes:

        if node.value is not None: #is not None
            if not node.parent.value: # is None
                node.parent.value = node.value
                node.parent.bestChildMove = node.move
            else:
                if node.parent.player == WHITE:
                    if node.value > node.parent.value:
                        node.parent.value = node.value
                        node.parent.bestChildMove = node.move
                    # Alpha beta pruning
                    #else:
                        #return
                else:
                    if node.value < node.parent.value:
                        node.parent.value = node.value
                        node.parent.bestChildMove = node.move
                    # Alpha beta pruning
                    #else:
                        #return
        else:
            minimax(node.children)
