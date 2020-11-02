from tkinter import *
from warehouse import Warehouse
from tiles import *
from cart import Cart
from random import choice
from time import sleep


class WarehouseDrawer:
    def __init__(self, warehouse: Warehouse):
        self.wh = warehouse
        self.root = Tk()
        self.root.title('Automated Warehouse')
        width = (self.wh.max_x + 1) * GUI.TILE_SIZE + self.wh.max_x * GUI.GRID_THICKNESS
        height = (self.wh.max_y + 1) * GUI.TILE_SIZE + self.wh.max_y * GUI.GRID_THICKNESS
        self.canvas = Canvas(self.root, bg=GUI.GRID_COLOR, width=width, height=height)

        self.shapes = []
        self.draw_outline()

        self.carts = []
        self.cart_shapes = []

        self.canvas.pack()

    def draw_outline(self):
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
                                                                  fill=tile.color,
                                                                  width=0))
                if tile.__class__ == Rack:
                    self.draw_rack_acces_point(tile, top_left)

            self.shapes.append(row_of_shapes)

    def draw_rack_acces_point(self, tile, top_left):
        verticies = []
        verticies.append(Point(top_left.x + (GUI.TILE_SIZE/2), top_left.y + (GUI.TILE_SIZE/2)))

        if tile.access_dir == '<':
            verticies.append(Point(top_left.x, top_left.y))
            verticies.append(Point(top_left.x, top_left.y + GUI.TILE_SIZE))
        elif tile.access_dir == '^':
            verticies.append(Point(top_left.x, top_left.y))
            verticies.append(Point(top_left.x + GUI.TILE_SIZE, top_left.y))
        elif tile.access_dir == '>':
            verticies.append(Point(top_left.x + GUI.TILE_SIZE, top_left.y))
            verticies.append(Point(top_left.x + GUI.TILE_SIZE, top_left.y + GUI.TILE_SIZE))
        elif tile.access_dir == 'v':
            verticies.append(Point(top_left.x, top_left.y + GUI.TILE_SIZE))
            verticies.append(Point(top_left.x + GUI.TILE_SIZE, top_left.y + GUI.TILE_SIZE))

        self.canvas.create_polygon(verticies[0].x, verticies[0].y,
                                   verticies[1].x, verticies[1].y,
                                   verticies[2].x, verticies[2].y,
                                   fill=tile.access_color,
                                   width=0)

    def draw_carts(self):
        for cart in self.cart_shapes:
            self.canvas.delete(cart)

        new_cart_shapes = []
        for cart in self.carts:
            self.draw_single_cart(cart, new_cart_shapes)
        self.cart_shapes = new_cart_shapes

    def draw_single_cart(self, cart, new_cart_shapes):
        top_left = Point(cart.act_tile.coords.x * (GUI.TILE_SIZE + GUI.GRID_THICKNESS),
                         cart.act_tile.coords.y * (GUI.TILE_SIZE + GUI.GRID_THICKNESS))
        top_left.x += (GUI.TILE_SIZE - GUI.CART_SIZE) // 2
        top_left.y += (GUI.TILE_SIZE - GUI.CART_SIZE) // 2
        movement_offset_x = abs(cart.act_tile.coords.x - cart.target_tile.coords.x) * \
                            (GUI.TILE_SIZE + GUI.GRID_THICKNESS) * \
                            cart.target_directions('x') * cart.movement_progress / 100
        movement_offset_y = abs(cart.act_tile.coords.y - cart.target_tile.coords.y) * \
                            (GUI.TILE_SIZE + GUI.GRID_THICKNESS) * \
                            cart.target_directions('y') * cart.movement_progress / 100
        top_left.x += movement_offset_x
        top_left.y += movement_offset_y
        bottom_right = Point(top_left.x + GUI.CART_SIZE,
                             top_left.y + GUI.CART_SIZE)
        new_cart_shapes.append(self.canvas.create_rectangle(top_left.x,
                                                            top_left.y,
                                                            bottom_right.x,
                                                            bottom_right.y,
                                                            fill=cart.color,
                                                            width=0))
        if cart.loaded:
            top_left.x += GUI.CART_SIZE/4
            top_left.y += GUI.CART_SIZE/4

            bottom_right.x -= GUI.CART_SIZE/4
            bottom_right.y -= GUI.CART_SIZE/4

            new_cart_shapes.append(self.canvas.create_rectangle(top_left.x,
                                                                top_left.y,
                                                                bottom_right.x,
                                                                bottom_right.y,
                                                                fill=cart.load_color,
                                                                width=0))

    def run(self, method):
        self.cart_handling_method = method
        self.root.after(0, self.animation)
        mainloop()

    def animation(self):
        while True:
            print('ch method')
            self.cart_handling_method()
            self.draw_carts()
            self.root.update()

            sleep(GUI.CYCLE_TIME)

    def motion_handling(self):
        for cart in self.carts:
            if not cart.is_path_done():
                cart.move_along_path()
            else:
                new_target = choice(self.wh.floors)
                while new_target == cart.target_tile:
                    new_target = choice(self.wh.floors)
                cart.set_path(new_target)
                cart.move_along_path()


if __name__ == '__main__':
    warehouse = Warehouse('wh1.txt')
    warehouse_drawer = WarehouseDrawer(warehouse)
    carts = []
    for _ in range(50):
        carts.append(Cart(choice(warehouse.starts), warehouse))
    warehouse_drawer.carts = carts

    warehouse_drawer.run(warehouse_drawer.motion_handling)
