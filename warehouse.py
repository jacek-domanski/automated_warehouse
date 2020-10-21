from tiles import *


class Warehouse:
    def __init__(self, file):
        self.matrix = self.read_file(file)

        self.tiles = dict()
        self.tiles['floors'] = []
        self.tiles['walls'] = []
        self.tiles['racks'] = []
        self.tiles['starts'] = []
        self.tiles['targets'] = []

        self.fill_tiles()

        for row in self.matrix:
            for tile in row:
                print(f'{tile.__class__.__name__}: {tile.coords.x}, {tile.coords.y}')

    def fill_tiles(self):
        for y, row in enumerate(self.matrix):
            for x, tile in enumerate(row):
                if tile == 'o':
                    self.tiles['floors'].append(Floor(x, y))
                    self.matrix[y][x] = self.tiles['floors'][-1]
                elif tile == 'x':
                    self.tiles['walls'].append(Wall(x, y))
                    self.matrix[y][x] = self.tiles['walls'][-1]
                elif tile in ['<', '>', '^', 'v']:
                    self.tiles['racks'].append(Rack(x, y, tile))
                    self.matrix[y][x] = self.tiles['racks'][-1]
                elif tile == 't':
                    self.tiles['targets'].append(Target(x, y))
                    self.matrix[y][x] = self.tiles['targets'][-1]
                elif tile == 's':
                    self.tiles['starts'].append(Start(x, y))
                    self.matrix[y][x] = self.tiles['starts'][-1]

    def read_file(self, file):
        matrix = []

        with open(file, 'r') as f:
            for line in f:
                row = list(line.strip())
                matrix.append(row)

        return matrix


if __name__ == '__main__':
    warehouse = Warehouse('wh1.txt')
