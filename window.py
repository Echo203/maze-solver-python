from tkinter import Tk, BOTH, Canvas
from line import Line


class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title = title
        self.canvas = Canvas(master=self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line: Line, color: str = "black"):
        line.draw(self.canvas, color)
