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

def print_board(board):
    w = len(board[0])+2
    print "="*w
    for line in board:
        print "|%s|" % "".join(map(lambda x: "x" if x else " ", line))
    print "="*w

if __name__=="__main__":
    print_board(board)