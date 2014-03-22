#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

import sys, os, time
import argparse
import logic, board

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Conway`s Game of Life')
    parser.add_argument('boardfile', type=str)
    parser.add_argument('-g', '--max-gens', type=int, help='maximum number of generations (default: 10)', default=10)
    parser.add_argument('-s', '--sleep-time', type=int, help='sleep time (default: 200 ms)', default=200)
    args = parser.parse_args()

    try:
         b = board.from_file(args.boardfile)
    except IOError:
        print "Could not find board file:", sys.argv[1]
        sys.exit(1)

    for gen in logic.generations(b, args.max_gens):
        os.system('cls' if os.name == 'nt' else 'clear')
        print board.to_string(gen)
        time.sleep(args.sleep_time / 1000.)
