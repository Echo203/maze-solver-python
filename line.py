from point import Point
from tkinter import Canvas


class Line:
    def __init__(self, point_one: Point, point_two: Point):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas: Canvas, color: str):
        canvas.create_line(
            self.point_one.x,
            self.point_one.y,
            self.point_two.x,
            self.point_two.y,
            fill=color,
            width=2,
        )
        print(f"DRAWING {color.capitalize()} LINE:")
        print(f"from x: {self.point_one.x} y: {self.point_one.y}")
        print(f"to   x: {self.point_two.x} y: {self.point_two.y}")
