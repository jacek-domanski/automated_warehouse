from misc import Point
from abc import ABC


class Tile(ABC):
    def __init__(self, x, y):
        self.coords = Point(x, y)
        self.connections = []


class Floor(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)


class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)


class Start(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)


class Target(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)


class Rack(Tile):
    def __init__(self, x, y, access_dir):
        super().__init__(x, y)
        if access_dir == '<':
            self.access_point = Floor(x-1, y)
        elif access_dir == '>':
            self.access_point = Floor(x+1, y)
        elif access_dir == 'v':
            self.access_point = Floor(x, y-1)
        elif access_dir == '^':
            self.access_point = Floor(x, y+1)
