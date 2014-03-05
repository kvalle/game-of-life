#!/usr/bin/env python

board = [
    [0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,0,1,1,0,0,1,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,0,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

def board_to_string(board):
    w = len(board[0])+2
    str_repr = "="*w + "\n"
    for line in board:
        str_repr += "|%s|\n" % \
            "".join(map(lambda x: "x" if x else " ", line))
    str_repr += "="*w + "\n"
    return str_repr 

def board_from_string(string):
    lines = string.split("\n")
    lines = map(lambda x: x.strip(), lines)
    lines = filter(bool, lines)
    lines = lines[1:-1]
    lines = map(lambda x: x[1:-1], lines)
    lines = map(lambda line: map(lambda x: 1 if x == 'x' else 0, line), lines)
    return lines

if __name__=="__main__":
    print board_to_string(board)