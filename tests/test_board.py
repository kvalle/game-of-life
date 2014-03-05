# -*- coding: utf-8 -*-

from nose.tools import assert_equals, assert_raises_regexp
import board

example = [
    [0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,0,1,1,0,0,1,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,0,1,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

def test_board_from_string():
    assert_equals(example, board.from_string("""
        ============
        |    xxx   |
        |      x   |
        |  xx  x   |
        |  xx      |
        |  xx      |
        |   xxxxx  |
        |          |
        ============
    """))

def test_board_to_from_string():
    assert_equals(example, 
        board.from_string(board.to_string(example)))
