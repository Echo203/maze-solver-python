from window import Window
from line import Line
from point import Point
from random import randint
from cell import Cell

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def create_random_point_on_screen() -> Point:
    return Point(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))


win = Window(SCREEN_WIDTH, SCREEN_HEIGHT, "XD")

cell_one = Cell(win)
cell_two = Cell(win)

cell_one.draw(10, 10, 50, 50)
cell_two.draw(50, 50, 80, 80)

cell_one.draw_move(cell_two)

win.wait_for_close()
