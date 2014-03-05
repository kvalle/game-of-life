def members(board):
    return [(x,y) for x in range(len(board)) for y in range(len(board[0]))]

def neighbours(pos):
    return [(x,y) for x in range(pos[0]-1,pos[0]+2)
                    for y in range(pos[1]-1, pos[1]+2)
                        if x != pos[0] or y != pos[1]]
