# -*- coding: utf-8 -*-

from nose.tools import assert_equals, assert_raises_regexp
from os.path import dirname, relpath, join

import logic

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

def test_next_board():
    b = [[0,0,0,0],
         [0,0,0,0],
         [0,0,1,0]]
