#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

import sys, os, time
import argparse
from itertools import islice

from game import board
from game.rules import Rules

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Conway`s Game of Life')
    parser.add_argument('boardfile', type=str)
    parser.add_argument('-g', '--max-gens', type=int, help='maximum number of generations (default: no limit)', default=None)
    parser.add_argument('-s', '--sleep-time', type=int, help='sleep time (default: 200 ms)', default=200)
    parser.add_argument('-w', '--wrap-edges', action='store_true', default=False, help='enable wrapping on board edges')
    args = parser.parse_args()

    try:
         b = board.from_file(args.boardfile)
    except IOError:
        print "Could not find board file:", sys.argv[1]
        sys.exit(1)

    rules = Rules(wrap=args.wrap_edges)

    iterations = rules.generations(b)
    if args.max_gens:
        iterations = islice(iterations, args.max_gens)

    for b in rules.take_while_changing(iterations):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print board.to_string(b)
            time.sleep(args.sleep_time / 1000.)
        except KeyboardInterrupt:
            sys.exit(0)
