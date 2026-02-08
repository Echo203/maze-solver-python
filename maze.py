from cell import Cell
from time import sleep
from random import seed as random_from_seed, randrange


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
        seed=None,
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
        self.seed = seed
        if not seed:
            self.seed = random_from_seed(seed)
        self.__breake_walls_r(0, 0)

    def __create_cells(self):
        for i in range(self.num_col):
            self.__cells.append([])
            for j in range(self.num_row):
                self.__cells[i].append(Cell(self.__win))
                self.__draw_cell(i, j)

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
        current_cell = self.__cells[i][j]
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

    def __break_wall_between(self, i1, i2, j1, j2):
        if (i2 - i1) == 1:
            self.__cells[i1][j1].has_right_wall = False
            self.__draw_cell(i1, j1)
            self.__cells[i2][j2].has_left_wall = False
            self.__draw_cell(i2, j2)
            return
        elif (i2 - i1) == -1:
            self.__cells[i1][j1].has_left_wall = False
            self.__draw_cell(i1, j1)
            self.__cells[i2][j2].has_right_wall = False
            self.__draw_cell(i2, j2)
            return
        elif (j2 - j1) == 1:
            self.__cells[i1][j1].has_bottom_wall = False
            self.__draw_cell(i1, j1)
            self.__cells[i2][j2].has_top_wall = False
            self.__draw_cell(i2, j2)
            return
        elif (j2 - j1) == -1:
            self.__cells[i1][j1].has_top_wall = False
            self.__draw_cell(i1, j1)
            self.__cells[i2][j2].has_bottom_wall = False
            self.__draw_cell(i2, j2)
            return

    def __breake_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            to_visit = []

            if i > 0 and not self.__cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self.num_col - 1 and not self.__cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self.num_row - 1 and not self.__cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if not to_visit:
                self.__draw_cell(i, j)
                return
            else:
                index_of_picked_cell = randrange(len(to_visit))
                picked_cell_coords = to_visit[index_of_picked_cell]
                self.__break_wall_between(
                    i, picked_cell_coords[0], j, picked_cell_coords[1]
                )
                self.__breake_walls_r(picked_cell_coords[0], picked_cell_coords[1])
