# -*- coding: utf-8 -*-

from nose.tools import assert_equals, assert_raises_regexp
from os.path import dirname, relpath, join

import board
import logic

board_file = join(dirname(relpath(__file__)), 'board.txt')
example = board.from_file(board_file)

def test_get_members():
    members = logic.members(example)
    assert_equals(70, len(members))
    assert_equals((0,0), members[0])
    assert_equals((6,9), members[-1])

def test_get_neighbours():
    expected = [
        (4,1), (4,2), (4,3),
        (5,1),        (5,3),
        (6,1), (6,2), (6,3)
    ]
    assert_equals(expected, logic.neighbours((5,2)))
