from window import Window
from line import Line
from point import Point
from random import randint

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def create_random_point_on_screen():
    return Point(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))


win = Window(SCREEN_WIDTH, SCREEN_HEIGHT, "XD")

win.wait_for_close()
