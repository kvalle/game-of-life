Just a simple implementation of [Conway's Game of Life](http://en.wikipedia.org/wiki/Conway's_Game_of_Life).

**Usage**

```
usage: life.py [-h] [-g MAX_GENS] [-s SLEEP_TIME] [-w] boardfile

positional arguments:
  boardfile

optional arguments:
  -h, --help            show this help message and exit
  -g MAX_GENS, --max-gens MAX_GENS
                        maximum number of generations (default: no limit)
  -s SLEEP_TIME, --sleep-time SLEEP_TIME
                        sleep time (default: 200 ms)
  -w, --wrap-edges      enable wrapping on board edges
```
