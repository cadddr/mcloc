__author__ = 'pb'
import grid
from agent import agent

fps = 30

global g
global a

def setup():
    size(768, 768)
    frameRate(fps)

    global g
    g = grid.generate()

    global a
    a = agent()

def draw():
    global g
    global a

    a.move(g)
    a.sense(g)

    grid.draw(g)

    a.draw()

def keyPressed():
    global a

    if key == 'r':
        a.auto = not a.auto

    if key == 'm':
        a.visible = not a.visible

    if key == 'h':
        grid.highlight = not grid.highlight

    if key == 'g':
        grid.show = not grid.show

    if key == 'o':
        grid.shape = []