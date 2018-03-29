import modules.findMoves as findMoves
from modules.models import board
import heapq

#If true, print steps in logic including board state for each step, path plans and failed paths
PRINTPROCESS = False

def printMassacrePath(boardState):
    path = findPath(boardState)
    pathString = ""
    for move in path:
        pathString = pathString + str(move[0]) + " -> " + str(move[1]) + "\n"

    print(pathString)


def findPath(boardState):
    currentBoardState = []
    for line in boardState:
        newline = []
        for tile in line:
            newline.append(tile)
        currentBoardState.append(newline)
    # copy list

    massacreMoves = []

    while (board.blackPiecesExist(currentBoardState)):
        # Logic for next move
        nextMove = findNextMove(currentBoardState)

        massacreMoves.append(nextMove)
        if PRINTPROCESS:
            print("move" + str(nextMove))
        currentBoardState = applyMove(nextMove, currentBoardState)
        if PRINTPROCESS:
            board.printBoardState(currentBoardState)

        # continue loop

    return massacreMoves


def findNextMove(boardState):
    nextMove = ()

    numMoves, possibleMoves = findMoves.findMoves(boardState)
    targetPieces = board.colourPiecesInfo(boardState, board.BLACK)

    # Find black piece to target
    targetPiece = targetPieces[0]  # Default target
    for piece in targetPieces:
        if piece.inDanger(boardState):
            targetPiece = piece  # Easier target

    # For all white pieces
    attackingPieces = board.colourPiecesInfo(boardState, board.WHITE)
    # Search for path from white piece to target black piece
    shortestPath = []
    shortestPathLength = -1

    for piece in attackingPieces:

        path = attackPath(boardState, piece.pos, targetPiece)
        if path:
            if (shortestPathLength == -1 or len(path) < shortestPathLength) and len(path) > 1:
                shortestPath = path
                shortestPathLength = len(path)
                attackingPiecePos = piece.pos
    # Path to kill = attackPath(boardState, start (white piece's location), finish  (target piece's location))
    # Keep track of shortest path

    if PRINTPROCESS:
        print("path" + str(shortestPath))
    # next move = path to kill [1]
    nextMove = shortestPath[1]

    # return first step in path
    return (attackingPiecePos, nextMove)


def applyMove(move, boardState):


    newBoardState = []
    for line in boardState:
        newline = []
        for tile in line:
            newline.append(tile)
        newBoardState.append(newline)
    # copy list

    # Get piece's colour
    colour = newBoardState[move[0][0]][move[0][1]]
    # Remove piece from original position
    newBoardState[move[0][0]][move[0][1]] = board.EMPTY

    # Add piece to destination
    newBoardState[move[1][0]][move[1][1]] = colour

    # Remove dead pieces
    newBoardState = wipeDeadPieces(newBoardState, colour)

    return newBoardState


def wipeDeadPieces(boardState, whosTurn):
    # Wipe opposing pieces (Before current turn's pieces!)
    for colour in [board.opposite(whosTurn), whosTurn]:
        for row in range(0, board.boardSize):
            for column in range(0, board.boardSize):
                if boardState[row][column] == colour:
                    # if surrounded vertically
                    if 0 < row < board.boardSize-1:
                        if (boardState[row - 1][column] == board.opposite(colour) or boardState[row - 1][
                            column] == board.CORNER) \
                                and (boardState[row + 1][column] == board.opposite(colour) or boardState[row + 1][
                            column] == board.CORNER):
                            boardState[row][column] = board.EMPTY  # Remove

                    # if surrounded horizontally
                    if 0 < column < board.boardSize-1:
                        if (boardState[row][column - 1] == board.opposite(colour) or (
                                boardState[row][column - 1] == board.CORNER)) \
                                and (boardState[row][column + 1] == board.opposite(colour) or boardState[row][
                            column + 1] == board.CORNER):
                            boardState[row][column] = board.EMPTY  # Remove

    return boardState


class PriorityQueue:
    #https: // www.redblobgames.com / pathfinding / a - star / implementation.html

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def attackPath(boardState, start, targetPiece):

    finish = targetPiece.pos

    # Find path from start to finish
    # Return false if path is impossible
    # Use some kind of search strategy

    #https: // www.redblobgames.com / pathfinding / a - star / implementation.html

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        #if targetPiece.inDanger and adjacent(current, finish):
        if targetPiece.adjacent(current):
            if not targetPiece.inDanger(boardState) or targetPiece.isLethal(current, applyMove((start,current), boardState)):
                # Return numMoves, path
                node = current
                path = [node]

                while node in came_from:
                    path.append(came_from[node])
                    node = came_from[node]
                path.reverse()

                return path

        # Next nodes/directions
        # Get finish position of all possible moves

        possibleMoves,_ = findMoves.onePiecePossibleMoves(boardState, board.piece(board.WHITE, current))
        nodes = [x[1] for x in possibleMoves]

        for next in nodes:
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(current, next)
                frontier.put(next, priority)
                came_from[next] = current
    if PRINTPROCESS:
        print("no path found from " + str(start) + " to " + str(finish))
    return False

#Heuristic - estimate of distance between two pieces
# row diff + column diff
def heuristic(start, finish):

    return abs(start[0]-finish[0]) + abs(start[1]-finish[1])

