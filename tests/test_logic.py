# -*- coding: utf-8 -*-

from nose.tools import assert_equals, assert_raises_regexp
from os.path import dirname, relpath, join

import logic, board

def test_get_members():
    b = [[0,1,1,1],
         [0,0,0,1],
         [1,1,1,1]]
    members = logic.members(b)
    assert_equals(12, len(members))
    assert_equals((0,0), members[0])
    assert_equals((2,3), members[-1])

def test_get_neighbours():
    expected = [(4,1), (4,2), (4,3),
                (5,1),        (5,3),
                (6,1), (6,2), (6,3)]
    assert_equals(expected, logic.neighbours((5,2)))

def test_get_value_from_board():
    b = [[0,0,0],
         [0,0,0],
         [0,0,1]]
    assert_equals(0, logic.value(b, (0,0)))
    assert_equals(1, logic.value(b, (2,2)))

def test_get_value_wraps():
    b = [[0,0,0,0],
         [0,0,0,0],
         [0,0,1,0]]
    assert_equals(1, logic.value(b, (2,2))) 
    assert_equals(1, logic.value(b, (2,6)))
    assert_equals(1, logic.value(b, (5,2)))
    assert_equals(1, logic.value(b, (-1,-2)))

def test_get_values():
    b = [[0,0,1],
         [0,1,1]]
    assert_equals([0,0,1,0,1,1], 
        logic.values(b, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]))

def test_next_board_starvation():
    b = [[0,0,0],
         [0,1,0],
         [0,0,0]]
    expected = \
        [[0,0,0],
         [0,0,0],
         [0,0,0]]
    assert_equals(expected, logic.next_board(b))

def test_next_board_reproduction():
    b = [[0,0,0,0,0],
         [0,0,1,0,0],
         [0,0,1,0,0],
         [0,0,1,0,0],
         [0,0,0,0,0]]
    expected = \
        [[0,0,0,0,0],
         [0,0,0,0,0],
         [0,1,1,1,0],
         [0,0,0,0,0],
         [0,0,0,0,0]]
    assert_equals(expected, logic.next_board(b))

def test_block_stable():
    block = [[0,0,0,0],
             [0,1,1,0],
             [0,1,1,0],
             [0,0,0,0]]
    result = logic.next_board(logic.next_board(logic.next_board(block)))
    assert_equals(block, result)

def test_beehive_stable():
    next = logic.next_board
    beehive = [[0,0,0,0,0,0],
               [0,0,1,1,0,0],
               [0,1,0,0,1,0],
               [0,0,1,1,0,0],
               [0,0,0,0,0,0]]
    result = next(next(next(beehive)))
    assert_equals(beehive, result)

def test_toad_period():
    next = logic.next_board
    first = [[0,0,0,0,0,0],
             [0,0,0,0,0,0],
             [0,0,1,1,1,0],
             [0,1,1,1,0,0],
             [0,0,0,0,0,0],
             [0,0,0,0,0,0]]
    expected_second = \
            [[0,0,0,0,0,0],
             [0,0,0,1,0,0],
             [0,1,0,0,1,0],
             [0,1,0,0,1,0],
             [0,0,1,0,0,0],
             [0,0,0,0,0,0]]

    second = next(first)
    third = next(second)

    assert_equals(expected_second, second)
    assert_equals(third, first)

def test_diehard_generations():
    diehard = board.from_string("""
        =================
        |               |
        |               |
        |               |
        |               |
        |               |
        |               |
        |          x    |
        |    xx         |
        |     x   xxx   |
        |               |
        |               |
        |               |
        |               |
        |               |
        |               |
        =================
    """)
    gens = list(logic.generations(diehard, limit=200))
    assert_equals(131, len(gens))
