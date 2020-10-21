from tiles import *


class Warehouse:
    def __init__(self, file):
        self.matrix = self.read_file(file)
        self.max_x = len(self.matrix[0]) - 1
        self.max_y = len(self.matrix) - 1

        self.floors = []
        self.walls = []
        self.racks = []
        self.starts = []
        self.targets = []
        self.tiles = [self.floors, self.walls, self.racks, self.starts, self.targets]

        self.fill_tiles()
        self.fill_connections()

    def read_file(self, file):
        matrix = []

        with open(file, 'r') as f:
            for line in f:
                row = list(line.strip())
                matrix.append(row)

        return matrix

    def fill_tiles(self):
        for y, row in enumerate(self.matrix):
            for x, tile in enumerate(row):
                if tile == 'o':
                    self.floors.append(Floor(x, y))
                    self.matrix[y][x] = self.floors[-1]
                elif tile == 'x':
                    self.walls.append(Wall(x, y))
                    self.matrix[y][x] = self.walls[-1]
                elif tile in ['<', '>', '^', 'v']:
                    self.racks.append(Rack(x, y, tile))
                    self.matrix[y][x] = self.racks[-1]
                elif tile == 't':
                    self.targets.append(Target(x, y))
                    self.matrix[y][x] = self.targets[-1]
                elif tile == 's':
                    self.starts.append(Start(x, y))
                    self.matrix[y][x] = self.starts[-1]

    def fill_connections(self):
        for row in self.matrix:
            for tile in row:
                self.append_passable_neighbours(tile)

    def append_passable_neighbours(self, tile):
        if tile.passable:
            for neighbour in self.generate_tile_neighbours(tile):
                if neighbour.passable:
                    tile.connections.append(neighbour)

    def generate_tile_neighbours(self, tile):
        x = tile.coords.x
        y = tile.coords.y

        offsets = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]

        for offset in offsets:
            new_x = x + offset.x
            new_y = y + offset.y

            if 0 <= new_x <= self.max_x and 0 <= new_y <= self.max_y:
                yield self.matrix[new_y][new_x]


if __name__ == '__main__':
    warehouse = Warehouse('wh1.txt')

    for tile_list in warehouse.tiles:
        for tile in tile_list:
            print(f'{tile.__class__.__name__}\t({tile.coords.x}, {tile.coords.y})\tn:{len(tile.connections)}')