# -*- coding: utf-8 -*-

from nose.tools import assert_equals, assert_raises_regexp
from os.path import dirname, relpath, join
from itertools import islice

from game.rules import Rules
from game.board import from_string

rules = Rules()

def test_get_members():
    b = [[0,1,1,1],
         [0,0,0,1],
         [1,1,1,1]]
    members = rules.members(b)
    assert_equals(12, len(members))
    assert_equals((0,0), members[0])
    assert_equals((2,3), members[-1])

def test_get_neighbours():
    expected = [(4,1), (4,2), (4,3),
                (5,1),        (5,3),
                (6,1), (6,2), (6,3)]
    assert_equals(expected, rules.neighbours((5,2)))

def test_get_neighbours_with_wrap():
    expected = [(-1, -1), (-1, 0), (-1, 1), 
                ( 0, -1),          ( 0, 1), 
                ( 1, -1), ( 1, 0), ( 1, 1)]
    assert_equals(expected, Rules(wrap=True).neighbours((0,0)))

def test_get_neighbours_no_wrap():
    expected = [         ( 0, 1), 
                ( 1, 0), ( 1, 1)]
    assert_equals(expected, Rules(wrap=False).neighbours((0,0)))

def test_get_value_from_board():
    b = [[0,0,0],
         [0,0,0],
         [0,0,1]]
    assert_equals(0, rules.value(b, (0,0)))
    assert_equals(1, rules.value(b, (2,2)))

def test_get_value_wraps():
    b = [[0,0,0,0],
         [0,0,0,0],
         [0,0,1,0]]
    assert_equals(1, rules.value(b, (2,2))) 
    assert_equals(1, rules.value(b, (2,6)))
    assert_equals(1, rules.value(b, (5,2)))
    assert_equals(1, rules.value(b, (-1,-2)))

def test_get_values():
    b = [[0,0,1],
         [0,1,1]]
    assert_equals([0,0,1,0,1,1], 
        rules.values(b, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]))

def test_next_board_starvation():
    b = [[0,0,0],
         [0,1,0],
         [0,0,0]]
    expected = \
        [[0,0,0],
         [0,0,0],
         [0,0,0]]
    assert_equals(expected, rules.next_board(b))

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
    assert_equals(expected, rules.next_board(b))

def test_block_stable():
    block = [[0,0,0,0],
             [0,1,1,0],
             [0,1,1,0],
             [0,0,0,0]]
    result = rules.next_board(rules.next_board(rules.next_board(block)))
    assert_equals(block, result)

def test_beehive_stable():
    next = rules.next_board
    beehive = [[0,0,0,0,0,0],
               [0,0,1,1,0,0],
               [0,1,0,0,1,0],
               [0,0,1,1,0,0],
               [0,0,0,0,0,0]]
    result = next(next(next(beehive)))
    assert_equals(beehive, result)

def test_toad_period():
    next = rules.next_board
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
    diehard = from_string("""
        ========================================
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                      x               |
        |                xx                    |
        |                 x   xxx              |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        |                                      |
        ========================================
    """)
    gens = rules.generations(diehard)
    gens = islice(gens, 200)
    gens = rules.take_while_changing(gens)
    assert_equals(131, len(list(gens)))
