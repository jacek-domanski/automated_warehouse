from misc import Point
from abc import ABC
import GUI


class AbstractTile(ABC):
    def __init__(self, x, y):
        self.coords = Point(x, y)
        self.connections = []
        self.passable = True  # if cart can go through this tile


class Floor(AbstractTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = GUI.FLOOR_COLOR


class Wall(AbstractTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.passable = False
        self.color = GUI.WALL_COLOR


class Start(AbstractTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = GUI.START_COLOR


class Target(AbstractTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = GUI.TARGET_COLOR


class Rack(AbstractTile):
    def __init__(self, x, y, access_dir):
        super().__init__(x, y)
        self.color = GUI.RACK_COLOR
        self.access_color = GUI.RACK_ACCESS_COLOR
        self.passable = False
        self.access_dir = access_dir

        if access_dir == '<':
            self.access_point = Floor(x-1, y)
        elif access_dir == '>':
            self.access_point = Floor(x+1, y)
        elif access_dir == 'v':
            self.access_point = Floor(x, y-1)
        elif access_dir == '^':
            self.access_point = Floor(x, y+1)
