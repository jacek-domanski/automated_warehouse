from tiles import *
from warehouse import Warehouse
from shortest_path import ShortestPath
from tiles import *
import GUI


class Cart:
    def __init__(self, spawning_tile: AbstractTile, warehouse: Warehouse):
        self.act_tile = spawning_tile
        self.target_tile = spawning_tile
        self.movement_progress = 0
        self.color = GUI.CART_COLOR
        self.load_color = GUI.CART_LOAD_COLOR

        self.loaded = False
        self.unloading = False

        self.wh = warehouse
        self.path_iterator = 0
        self.path = []
        self.shortest_path = ShortestPath(self.wh.matrix)

    def set_path(self, target_tile: AbstractTile):
        print('setting new path')
        self.path_iterator = 0
        self.path = self.shortest_path.find(self.act_tile.coords, target_tile.coords)
        self.set_target(self.path[self.path_iterator])

    def move_along_path(self):
        print('move along path called')
        if self.is_moving():
            print('moving along path')
            self.move()
        elif not self.is_path_done():
            print('setting new target, then moving along')
            self.path_iterator += 1
            self.set_target(self.path[self.path_iterator])
            self.move()

    def is_path_done(self):
        print(f'Checking if path done. Path iterator: {self.path_iterator} vs path len: {len(self.path)}')
        try:
            self.path[-1]
        except IndexError:
            return True
        print(f'Checking if path done: {self.act_tile == self.path[-1]}')
        return self.act_tile == self.path[-1]

    def set_target(self, target_tile: AbstractTile):
        self.movement_progress = 0
        self.target_tile = target_tile

    def move(self):
        if self.act_tile == self.target_tile:
            return

        self.movement_progress += GUI.CART_VELO

        if self.movement_progress >= 100:
            self.movement_progress = 100
            self.act_tile = self.target_tile

    def target_directions(self, axis):
        """Returns -1,0,1 for x or y depending on the relation of target tile"""

        if axis == 'x':
            act = self.act_tile.coords.x
            target = self.target_tile.coords.x
        elif axis == 'y':
            act = self.act_tile.coords.y
            target = self.target_tile.coords.y
        else:
            raise ValueError(f'x or y expected, got {axis} instead')

        if target < act:
            direction = -1
        elif target > act:
            direction = 1
        else:
            direction = 0

        return direction

    def is_moving(self):
        return self.act_tile != self.target_tile

    def unload(self):
        if not self.unloading:
            self.unloading = True
            self.set_target(self.wh.matrix[self.act_tile.coords.y][self.act_tile.coords.x-2])

        self.move()
        if not self.is_moving():
            self.unloading = False
            self.loaded = False


