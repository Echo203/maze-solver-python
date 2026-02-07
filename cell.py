from window import Window
from helpers import create_line_with_coordinates
from typing import Self


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

    def get_coords(self):
        return [self.__x1, self.__y1, self.__x2, self.__y2]

    def get_center(self):
        return [int((self.__x1 + self.__x2) / 2), int((self.__y1 + self.__y2) / 2)]

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.has_bottom_wall:
            self.__win.draw_line(create_line_with_coordinates(x1, y2, x2, y2))

        if self.has_left_wall:
            self.__win.draw_line(create_line_with_coordinates(x1, y1, x1, y2))

        if self.has_top_wall:
            self.__win.draw_line(create_line_with_coordinates(x1, y1, x2, y1))

        if self.has_right_wall:
            self.__win.draw_line(create_line_with_coordinates(x2, y1, x2, y2))

    def draw_move(self, to_cell: Self, undo=False):
        color = "red"
        if undo:
            color = "gray"

        center_one = self.get_center()
        center_two = to_cell.get_center()
        self.__win.draw_line(
            create_line_with_coordinates(
                center_one[0], center_one[1], center_two[0], center_two[1]
            ),
            color,
        )
