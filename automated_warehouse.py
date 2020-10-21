from warehouse import Warehouse
from random import choice
from shortest_path import ShortestPath


class AutomatedWarehouse:
    def __init__(self, file):
        self.warehouse = Warehouse(file)

    def run(self):
        shortest_path = ShortestPath(self.warehouse.matrix)
        a = choice(self.warehouse.starts)
        b = choice(self.warehouse.racks)
        shortest_path.find(a, b)


if __name__ == '__main__':
    automated_warehouse = AutomatedWarehouse('wh1.txt')
    automated_warehouse.run()
