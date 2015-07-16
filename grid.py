__author__ = 'pb'

from random import random

cell = 64
sparsity = .8
highlight = False
show = False

def pixels(cells):
    return cells * cell

def cells(pixels):
    return pixels / cell

def edge(x, y):
    return x not in range(1, cells(width) - 1) or y not in range(1, cells(height) - 1)

def vicinity(dim, x, range):
    return dim[x - range : x + range + 1]

def maybe_block(x, y):
    return 0 if edge(x, y) or random() > sparsity else 1.

def generate():
    return [[maybe_block(x, y) for x in range(cells(width))] for y in range(cells(height))]

def reduce_by(grid, reducer):
    return reduce(lambda a, b: a + reducer(b), [0.] + grid)

def draw_cell(grid, x, y):
    if show:
        stroke(0)
    else:
        noStroke()

    #if not grid[y][x] and not edge(x, y) and highlight:
     #   fill(15, 0, 0)
    #else:
    fill(fade(grid[y][x]) + 7 * (grid[y][x] and highlight))

    rect(pixels(x), pixels(y), cell, cell)

def fade(rate):
    return 3 * 255 * rate

def draw(grid):
    mass = reduce_by(grid, sum)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            # normalize
            grid[y][x] /= mass
            # relative scale evil
            #grid[y][x] /= reduce_by(grid, max)


    #absolute = reduce_by(grid, max)
    #for y in range(len(grid)):
    #    for x in range(len(grid[0])):
    #        grid[y][x] /= absolute

            draw_cell(grid, x, y)