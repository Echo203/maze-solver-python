from cell import Cell
from time import sleep


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_row: int,
        num_col: int,
        cell_size_x: int,
        cell_size_y: int,
        win=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.num_row = num_row
        self.num_col = num_col
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()

    def __create_cells(self):
        for i in range(self.num_col):
            self.__cells.append([])
            for j in range(self.num_row):
                self.__cells[i].append(Cell(self.__win))
                self.__draw_cell(j, i)

    def __draw_cell(self, i, j):
        if not self.__win:
            return

        # x1, y1, x2, y2
        coords_of_cell = [
            self.__x1 + self.cell_size_x * i,
            self.__y1 + self.cell_size_y * j,
            self.__x1 + self.cell_size_x * (i + 1),
            self.__y1 + self.cell_size_y * (j + 1),
        ]
        current_cell = self.__cells[j][i]
        current_cell.draw(
            coords_of_cell[0], coords_of_cell[1], coords_of_cell[2], coords_of_cell[3]
        )
        self.__animate()

    def __animate(self):
        if not self.__win:
            return
        self.__win.redraw()
        # sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.num_col - 1][self.num_row - 1].has_bottom_wall = False
        self.__draw_cell(self.num_col - 1, self.num_row - 1)
