from window import Window
from point import Point
from random import randint
from cell import Cell
from maze import Maze
from tkinter import Tk, BOTH, Frame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


def create_random_point_on_screen() -> Point:
    return Point(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))


win = Window(SCREEN_WIDTH, SCREEN_HEIGHT, "XD")

# win.root.geometry("800x600")  # You want the size of the app to be 500x500
# # win.root.resizable(False, False)

# back = Frame(master=win.root, bg="white")
# back.pack_propagate(True)
# back.pack(expand=True)

# cell_one = Cell(win)
# cell_two = Cell(win)

# cell_one.draw(10, 10, 50, 50)
# cell_two.draw(50, 50, 80, 80)

# cell_one.draw_move(cell_two)

my_maze = Maze(2, 2, 10, 10, 20, 20, win, 498)
my_maze.solve()


win.wait_for_close()
