from cell import Cell
from random import seed as random_from_seed, randrange
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
        if seed:
            random_from_seed(seed)
        self.__breake_walls_r(0, 0)
        self.__reset_cells_visited()

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

    def __animate(self, delay=False):
        if not self.__win:
            return
        self.__win.redraw()
        if delay:
            sleep(0.05)

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

    def __reset_cells_visited(self):
        for i in range(self.num_col):
            for j in range(self.num_row):
                self.__cells[i][j].visited = False

    def solve(self, alg):
        match alg:
            case "dfs":
                return self.__solver_dfs_r(0, 0)
            case "bfs":
                self.__solver_bfs_r(0, 0)

    def __solver_dfs_r(self, x, y):
        self.__animate(True)

        current_cell: Cell = self.__cells[x][y]
        current_cell.visited = True

        if current_cell == self.__cells[self.num_col - 1][self.num_row - 1]:
            return True

        # Check left
        if (
            x != 0
            and not current_cell.has_left_wall
            and not self.__cells[x - 1][y].visited
        ):
            neighbour = self.__cells[x - 1][y]
            current_cell.draw_move(neighbour)
            result = self.__solver_dfs_r(x - 1, y)

            if result:
                return True

            current_cell.draw_move(neighbour, True)

        # Check top
        if (
            y != 0
            and not current_cell.has_top_wall
            and not self.__cells[x][y - 1].visited
        ):
            neighbour = self.__cells[x][y - 1]
            current_cell.draw_move(neighbour)
            result = self.__solver_dfs_r(x, y - 1)

            if result:
                return True

            current_cell.draw_move(neighbour, True)

        # Check right
        if (
            (x != self.num_col - 1)
            and not current_cell.has_right_wall
            and not self.__cells[x + 1][y].visited
        ):
            neighbour = self.__cells[x + 1][y]
            current_cell.draw_move(neighbour)
            result = self.__solver_dfs_r(x + 1, y)

            if result:
                return True

            current_cell.draw_move(neighbour, True)

        # Check bottom
        if (
            (y != self.num_row - 1)
            and not current_cell.has_bottom_wall
            and not self.__cells[x][y + 1].visited
        ):
            neighbour = self.__cells[x][y + 1]
            current_cell.draw_move(neighbour)
            result = self.__solver_dfs_r(x, y + 1)

            if result:
                return True

            current_cell.draw_move(neighbour, True)

        return False

    def generate_list_of_moves_from_cell(self, x, y):
        current_cell = self.__cells[x][y]
        moves = []
        # Check left
        if (
            x != 0
            and not current_cell.has_left_wall
            and not self.__cells[x - 1][y].visited
        ):
            moves.append((x - 1, y))

        # Check top
        if (
            y != 0
            and not current_cell.has_top_wall
            and not self.__cells[x][y - 1].visited
        ):
            moves.append((x, y - 1))

        # Check right
        if (
            (x != self.num_col - 1)
            and not current_cell.has_right_wall
            and not self.__cells[x + 1][y].visited
        ):
            moves.append((x + 1, y))

        # Check bottom
        if (
            (y != self.num_row - 1)
            and not current_cell.has_bottom_wall
            and not self.__cells[x][y + 1].visited
        ):
            moves.append((x, y + 1))

        return moves

    def __bfs_backtracker(self, routes, entrance, exit):
        # Start a list to represent path, starting at exit
        path = [exit]

        # Loop thorugh routes, till we get to the entrance
        while path[-1] != entrance:
            path.append(routes[path[-1]])

        for i in range(len(path) - 1, 0, -1):
            self.__animate(True)
            cell = path[i]
            next_cell = path[i - 1]
            self.__cells[cell[0]][cell[1]].draw_move(
                self.__cells[next_cell[0]][next_cell[1]]
            )

    def __solver_bfs_r(self, x, y):

        exit_cell = (self.num_col - 1, self.num_row - 1)

        parent = {}
        queue = []
        queue.append((x, y))

        while queue:
            self.__animate(True)

            cell = queue.pop(0)
            self.__cells[cell[0]][cell[1]].visited = True
            if cell == exit_cell:
                self.__bfs_backtracker(parent, (0, 0), exit_cell)
                return
            moves = self.generate_list_of_moves_from_cell(cell[0], cell[1])
            for move in moves:
                if move not in queue:
                    self.__cells[cell[0]][cell[1]].draw_move(
                        self.__cells[move[0]][move[1]], True
                    )
                    parent[move] = cell
                    queue.append(move)
