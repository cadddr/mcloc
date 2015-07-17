__author__ = 'pb'
from grid import cell, pixels, vicinity, reduce_by
from random import random

sense_range = 1
sense_prob = .9
move_prob = .9

class agent(object):
    pos = PVector(2, 2)
    speed = PVector(1, 0)

    auto = False
    visible = True

    def sense(self, grid):
        def look_around(grid, pos, range):
            return [[not x
                     for x in vicinity(row, int(pos.x), range)]
                    for row in vicinity(grid, int(pos.y), range)]

        around = look_around(grid, self.pos, sense_range)

        for y in range(sense_range, len(grid) - sense_range):
            for x in range(sense_range, len(grid[0]) - sense_range):
                if grid[y][x]:
                    hit = (around == look_around(grid, PVector(x, y), sense_range)) if random() < sense_prob else 1
                    grid[y][x] *= hit * sense_prob + (1 - hit) * (1 - sense_prob)

    def move(self, grid):
        if not self.auto:
            return

        def turn():
            vertical = random() > .5
            self.speed = PVector((not vertical) * (1 if random() > .5 else -1), vertical * (1 if random() > .5 else -1))

        while 1:
            new = self.pos + self.speed
            if (grid[int(new.y)][int(new.x)]):
                break
            turn()

        # belief update
        for y in range(1, len(grid) - 1):
            for x in range(1, len(grid[0]) - 1):
                if grid[y][x]:
                    grid[y][x] = grid[int(y - self.speed.y)][int(x - self.speed.x)] * move_prob + grid[y][x] * (1 - move_prob)

        self.pos = new

    def draw(self):
        if not self.visible:
            return

        stroke(204, 104, 10)
        noFill()
        strokeWeight(4)

        rect(pixels(self.pos.x),
             pixels(self.pos.y),
             cell,
             cell)