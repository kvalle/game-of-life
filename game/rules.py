# ~*~ encoding: utf-8 ~*~

DEFAULT_WRAP = False

class Rules:

    def members(self, board):
        return [(x,y) for x in range(len(board)) 
                        for y in range(len(board[0]))]

    def neighbours(self, pos, wrap=DEFAULT_WRAP):
        neighbours=  [(x,y) for x in range(pos[0]-1,pos[0]+2)
                                for y in range(pos[1]-1, pos[1]+2)
                                    if x != pos[0] or y != pos[1]]
        if not wrap:
            neighbours = filter(lambda (x,y): x>=0 and y>=0, neighbours)

        return neighbours

    def value(self, board, p):
        x = p[0] % len(board)
        y = p[1] % len(board[0])
        return board[x][y]

    def values(self, board, ps):
        return [self.value(board, p) for p in ps]

    def new_value(self, old_val, sum_neighbours):
        if old_val == 1 and sum_neighbours in [2,3]:
            return 1
        if old_val == 0 and sum_neighbours == 3:
            return 1
        return 0

    def next_val(self, board, pos, wrap=DEFAULT_WRAP):
        sum_neighbours = sum([self.value(board, n) 
                                for n in self.neighbours(pos, wrap)])
        old_val = self.value(board, pos)
        return self.new_value(old_val, sum_neighbours)

    def empty_board(self, x,y):
        return [[0]*y for _ in range(x)]

    def next_board(self, board, wrap=DEFAULT_WRAP):
        b = self.empty_board(len(board), len(board[0]))
        for (x,y) in self.members(board):
            b[x][y] = self.next_val(board, (x,y), wrap)
        return b

    def generations(self, board, wrap=DEFAULT_WRAP):
        while True:
            board = self.next_board(board, wrap)
            yield board

    def take_while_changing(self, iterations):
        prev = None
        for b in iterations:
            yield b
            if b == prev:
                break
            prev = b
