def parse():

    boardState = []

    for i in range(0,8):
        row = input()
        row = row.split(" ")
        boardState.append(row)

    option = input()
    return (boardState, option)