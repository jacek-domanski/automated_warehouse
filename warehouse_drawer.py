from tkinter import *
from warehouse import Warehouse
import GUI
from tiles import *


class WarehouseDrawer:
    def __init__(self, warehouse: Warehouse):
        self.wh = warehouse
        self.root = Tk()
        width = (self.wh.max_x + 1) * GUI.TILE_SIZE + self.wh.max_x * GUI.GRID_THICKNESS
        height = (self.wh.max_y + 1) * GUI.TILE_SIZE + self.wh.max_y * GUI.GRID_THICKNESS
        self.canvas = Canvas(self.root, bg=GUI.GRID_COLOR, width=width, height=height)

        self.shapes = []
        for y, row in enumerate(self.wh.matrix):
            row_of_shapes = []
            for x, tile in enumerate(row):
                top_left = Point(x * (GUI.TILE_SIZE + GUI.GRID_THICKNESS),
                                 y * (GUI.TILE_SIZE + GUI.GRID_THICKNESS))
                bottom_right = Point(top_left.x + GUI.TILE_SIZE,
                                     top_left.y + GUI.TILE_SIZE)
                row_of_shapes.append(self.canvas.create_rectangle(top_left.x,
                                                                  top_left.y,
                                                                  bottom_right.x,
                                                                  bottom_right.y,
                                                                  fill=tile.color))
            self.shapes.append(row_of_shapes)

        self.canvas.pack()
        mainloop()

    def run(self):
        pass


if __name__ == '__main__':
    warehouse = Warehouse('wh1.txt')
    warehouse_drawer = WarehouseDrawer(warehouse)
    warehouse_drawer.run()
