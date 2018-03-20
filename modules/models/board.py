BLACK = "@"
WHITE = "O"
EMPTY = "-"
CORNER = "X"

boardSize = 8


def blackPiecesExist(boardState):
    for row in boardState:
        for tile in row:
            if tile == BLACK:
                return False
    return True