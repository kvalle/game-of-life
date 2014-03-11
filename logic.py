def members(board):
    return [(x,y) for x in range(len(board)) for y in range(len(board[0]))]

def neighbours(pos):
    return [(x,y) for x in range(pos[0]-1,pos[0]+2)
                    for y in range(pos[1]-1, pos[1]+2)
                        if x != pos[0] or y != pos[1]]

def value(board, p):
    x = p[0] % len(board)
    y = p[1] % len(board[0])
    return board[x][y]

def values(board, ps):
    return [value(board, p) for p in ps]

def new_value(old_val, sum_neighbours):
    if old_val == 1 and sum_neighbours in [2,3]:
        return 1
    if old_val == 0 and sum_neighbours == 3:
        return 1
    return 0

def next_val(board, pos):
    sum_neighbours = sum([value(board, n) for n in neighbours(pos)])
    old_val = value(board, pos)
    return new_value(old_val, sum_neighbours)

def empty_board(x,y):
    return [[0]*y for _ in range(x)]

def next_board(board):
    b = empty_board(len(board), len(board[0]))
    for (x,y) in members(board):
        b[x][y] = next_val(board, (x,y))
    return b
