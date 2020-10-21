from misc import Point
from abc import ABC


class AbstractTile(ABC):
    def __init__(self, x, y):
        self.coords = Point(x, y)
        self.connections = []
        self.passable = True  # if cart can go through this tile


class Floor(AbstractTile):
    def __init__(self, x, y):
        super().__init__(x, y)


class Wall(AbstractTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.passable = False


class Start(AbstractTile):
    def __init__(self, x, y):
        super().__init__(x, y)


class Target(AbstractTile):
    def __init__(self, x, y):
        super().__init__(x, y)


class Rack(AbstractTile):
    def __init__(self, x, y, access_dir):
        super().__init__(x, y)
        self.passable = False

        if access_dir == '<':
            self.access_point = Floor(x-1, y)
        elif access_dir == '>':
            self.access_point = Floor(x+1, y)
        elif access_dir == 'v':
            self.access_point = Floor(x, y-1)
        elif access_dir == '^':
            self.access_point = Floor(x, y+1)
