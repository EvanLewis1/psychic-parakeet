import modules.findMoves as findMoves
from modules.models import board_old
import heapq

#If true, print steps in logic including board state for each step, path plans and failed paths
PRINTPROCESS = False

def printMassacrePath(boardState):
    path = findPath(boardState)
    pathString = ""
    path = [[(x, y) for y, x in move] for move in path]

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

    while (board_old.blackPiecesExist(currentBoardState)):
        # Logic for next move
        nextMove = findNextMove(currentBoardState)

        massacreMoves.append(nextMove)
        if PRINTPROCESS:
            print("move" + str(nextMove))
        currentBoardState = applyMove(nextMove, currentBoardState)
        if PRINTPROCESS:
            board_old.printBoardState(currentBoardState)

        # continue loop

    return massacreMoves


def findNextMove(boardState):
    nextMove = ()

    numMoves, possibleMoves = findMoves.findMoves(boardState)
    targetPieces = board_old.colourPiecesInfo(boardState, board_old.BLACK)

    prioritisedTargetPieces = [piece for piece in targetPieces if piece.inDanger(boardState)]
    prioritisedTargetPieces = prioritisedTargetPieces + [piece for piece in targetPieces if not piece.inDanger(boardState)]

    # Find black piece to target
    for targetPiece in prioritisedTargetPieces:

        # For all white pieces
        attackingPieces = board_old.colourPiecesInfo(boardState, board_old.WHITE)
        # Search for path from white piece to target black piece
        shortestPath = []
        shortestPathLength = -1

        for piece in attackingPieces:

            path = attackPath(boardState, piece, targetPiece)
            if path:
                if (shortestPathLength == -1 or len(path) < shortestPathLength) and len(path) > 1:
                    shortestPath = path
                    shortestPathLength = len(path)
                    attackingPiecePos = piece.pos
        # Path to kill = attackPath(boardState, start (white piece's location), finish  (target piece's location))
        # Keep track of shortest path

        if PRINTPROCESS:
            print("path" + str(shortestPath))


        if len(shortestPath) > 1:
            nextMove = shortestPath[1]
            break

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
    newBoardState[move[0][0]][move[0][1]] = board_old.EMPTY

    # Add piece to destination
    newBoardState[move[1][0]][move[1][1]] = colour

    # Remove dead pieces
    newBoardState = wipeDeadPieces(newBoardState, colour)

    return newBoardState


def wipeDeadPieces(boardState, whosTurn):
    # Wipe opposing pieces (Before current turn's pieces!)
    for colour in [board_old.opposite(whosTurn), whosTurn]:
        for row in range(0, board_old.boardSize):
            for column in range(0, board_old.boardSize):
                if boardState[row][column] == colour:
                    # if surrounded vertically
                    if 0 < row < board_old.boardSize-1:
                        if (boardState[row - 1][column] == board_old.opposite(colour) or boardState[row - 1][
                            column] == board_old.CORNER) \
                                and (boardState[row + 1][column] == board_old.opposite(colour) or boardState[row + 1][
                                column] == board_old.CORNER):
                            boardState[row][column] = board_old.EMPTY  # Remove

                    # if surrounded horizontally
                    if 0 < column < board_old.boardSize-1:
                        if (boardState[row][column - 1] == board_old.opposite(colour) or (
                                boardState[row][column - 1] == board_old.CORNER)) \
                                and (boardState[row][column + 1] == board_old.opposite(colour) or boardState[row][
                                column + 1] == board_old.CORNER):
                            boardState[row][column] = board_old.EMPTY  # Remove

    return boardState


class PriorityQueue:
    # Taken from
    # https: // www.redblobgames.com / pathfinding / a - star / implementation.html

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def attackPath(boardState, attackingPiece, targetPiece):
    start = attackingPiece.pos
    finish = targetPiece.pos

    # Find path from start to finish
    # Return false if path is impossible
    # Use some kind of search strategy

    # Based on a* structure from
    # https: // www.redblobgames.com / pathfinding / a - star / implementation.html

    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        # if targetPiece.inDanger and adjacent(current, finish):
        if targetPiece.adjacent(current):
            if not targetPiece.inDanger(boardState) or targetPiece.isLethal(current, applyMove((start, current), boardState)):
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

        possibleMoves,_ = findMoves.onePiecePossibleMoves(boardState, board_old.piece(board_old.WHITE, current))
        safeMoves = [move for move in possibleMoves if len(board_old.colourPiecesInfo(boardState, board_old.WHITE)) == len(board_old.colourPiecesInfo(applyMove((start, move[1]), boardState), board_old.WHITE))]
        nodes = [x[1] for x in safeMoves]

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


# Heuristic - estimate of distance between two pieces
# row diff + column diff
def heuristic(start, finish):

    return abs(start[0]-finish[0]) + abs(start[1]-finish[1])

