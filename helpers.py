from point import Point
from line import Line


def create_line_with_coordinates(x1: int, y1: int, x2: int, y2: int) -> Line:
    return Line(Point(x1, y1), Point(x2, y2))
