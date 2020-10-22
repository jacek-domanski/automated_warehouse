from warehouse import Warehouse
from random import choice
from shortest_path import ShortestPath


class AutomatedWarehouse:
    def __init__(self, file):
        self.warehouse = Warehouse(file)

    def run(self):
        # shortest_path = ShortestPath(self.warehouse.matrix)
        # a = choice(self.warehouse.starts)
        # b = choice(self.warehouse.racks)
        # shortest_path.find(a, b)

        a = self.warehouse.matrix[1][0].coords
        b = self.warehouse.matrix[4][2].coords
        shortest_path = ShortestPath(self.warehouse.matrix)
        path = shortest_path.find(a, b)

        print(f'Shortest path from {a} to {b}:')
        for point in path:
            print(f'{point}')


if __name__ == '__main__':
    automated_warehouse = AutomatedWarehouse('wh1.txt')
    automated_warehouse.run()
