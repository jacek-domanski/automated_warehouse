from tiles import *


class Node:
    def __init__(self):
        self.links = []
        self.cost = float('inf')

    def add_links(self, all_nodes, tile_neighbours):
        for n in tile_neighbours:
            x = n.coords.x
            y = n.coords.y
            self.links.append(all_nodes[y][x])


class ShortestPath:
    def __init__(self, matrix):
        self.nodes = []

        self.add_nodes(matrix)

        for y, row in enumerate(self.nodes):
            for x, node in enumerate(row):
                node.add_links(self.nodes, matrix[y][x].connections)

    def add_nodes(self, matrix):
        for row_of_tiles in matrix:
            row_of_nodes = []
            for _ in row_of_tiles:
                row_of_nodes.append(Node())
            self.nodes.append(row_of_nodes)

    def find(self, a, b):
        pass
        # Nothing was tested yet