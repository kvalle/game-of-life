#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

import sys, os, time
import argparse
import logic, board
from itertools import islice

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Conway`s Game of Life')
    parser.add_argument('boardfile', type=str)
    parser.add_argument('-g', '--max-gens', type=int, help='maximum number of generations (default: no limit)', default=None)
    parser.add_argument('-s', '--sleep-time', type=int, help='sleep time (default: 200 ms)', default=200)
    args = parser.parse_args()

    try:
         b = board.from_file(args.boardfile)
    except IOError:
        print "Could not find board file:", sys.argv[1]
        sys.exit(1)

    iterations = logic.generations(b)
    if args.max_gens:
        iterations = islice(iterations, args.max_gens)

    for b in logic.take_while_changing(iterations):
        os.system('cls' if os.name == 'nt' else 'clear')
        print board.to_string(b)
        time.sleep(args.sleep_time / 1000.)
