__author__ = 'pb'
from grid import cell, pixels, vicinity, reduce_by
from random import random

sense_range = 1
sense_prob = .7
move_prob = 1.


class agent(object):
    pos = PVector(2, 2)
    #prev = PVector(0, 0)
    speed = PVector(1, 0)

    auto = False
    visible = True

    def sense(self, grid):
        def look_around(grid, pos, range):
            def maybe_see_something(x):
                # TODO:
                return not x# if random() < sense_prob else x

            return [[maybe_see_something(x)
                     for x in vicinity(row, int(pos.x), range)]
                    for row in vicinity(grid, int(pos.y), range)]

        around = look_around(grid, self.pos, sense_range)

        for y in range(sense_range, len(grid) - sense_range):
            for x in range(sense_range, len(grid[0]) - sense_range):
                if grid[y][x]:
                    hit = around == look_around(grid, PVector(x, y), sense_range)
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

        #temp = [[0. for x in grid[0]] for y in grid]

        # belief update
        for y in range(1, len(grid) - 1):
            for x in range(1, len(grid[0]) - 1):
                if grid[y][x]:
                    grid[y][x] = grid[int(new.y)][int(new.x)] * move_prob #+ grid[int(new.y)][int(new.x)] * (1 - move_prob) #/ (sqrt((y - self.pos.y) ** 2 + (x - self.pos.x) ** 2) + .001)

        #grid = temp
        #self.prev = self.pos
        self.pos = new



        #grid[int(self.pos.y)][int(self.pos.x)] = grid[int(self.prev.y)][int(self.prev.x)] * move_prob

    def draw(self):
        if not self.visible:
            return

        stroke(204, 104, 10)
        noFill()
        strokeWeight(4)

        rect(pixels(self.pos.x), #+ cell / 2,
             pixels(self.pos.y), #+ cell / 2,
             cell,
             cell)