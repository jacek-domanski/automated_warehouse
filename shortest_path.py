from tiles import *


class Node:
    def __init__(self, tile):
        self.tile = tile
        self.links = []
        self.reset()

    def add_links(self, all_nodes):
        for neighbour in self.tile.connections:
            x = neighbour.coords.x
            y = neighbour.coords.y
            self.links.append(all_nodes[y][x])

    def reset(self):
        self.cost = float('inf')
        self.best_from = None


class ShortestPath:
    """Finds cheapest path from a to b"""
    def __init__(self, matrix):
        self.nodes = []

        self.__add_nodes(matrix)
        self.__add_links_to_nodes()

        self.a = None
        self.b = None
        self.cost = 0

    def __add_nodes(self, matrix):
        for row_of_tiles in matrix:
            row_of_nodes = []
            for tile in row_of_tiles:
                row_of_nodes.append(Node(tile))
            self.nodes.append(row_of_nodes)

    def __add_links_to_nodes(self):
        for row in self.nodes:
            for node in row:
                node.add_links(self.nodes)

    def find(self, a: Point, b: Point):
        """Main method that returns cheapest way as a list of Points"""
        self.__setup(a, b)
        self.__start_dijkstra()
        return self.__build_path()

    def __setup(self, a, b):
        self.__reset_nodes()
        self.a = a
        self.b = b

    def __reset_nodes(self):
        for row in self.nodes:
            for node in row:
                node.reset()

    def __start_dijkstra(self):
        self.starting_node = self.nodes[self.a.y][self.a.x]
        self.starting_node.cost = 0
        self.__check_node(self.starting_node)

    def __check_node(self, node):
        for link in node.links:
            if node.cost+1 < link.cost:
                link.best_from = node
                link.cost = node.cost+1

                self.__check_node(link)

    def __build_path(self):
        path = []
        node = self.nodes[self.b.y][self.b.x]

        while node != self.starting_node:
            path.insert(0, node.tile)
            node = node.best_from

        return path
