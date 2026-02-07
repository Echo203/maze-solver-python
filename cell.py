from window import Window
from helpers import create_line_with_coordinates


class Cell:
    def __init__(self, window: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.has_bottom_wall:
            self.__win.draw_line(create_line_with_coordinates(x1, y1, x1, y2))

        if self.has_left_wall:
            self.__win.draw_line(create_line_with_coordinates(x1, y1, x2, y1))

        if self.has_top_wall:
            self.__win.draw_line(create_line_with_coordinates(x2, y1, x2, y2))

        if self.has_right_wall:
            self.__win.draw_line(create_line_with_coordinates(x1, y2, x2, y2))
