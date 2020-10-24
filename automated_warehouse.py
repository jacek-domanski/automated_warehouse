from warehouse import Warehouse
from random import choice
from warehouse_drawer import WarehouseDrawer
from cart import Cart


class AutomatedWarehouse:
    def __init__(self, file):
        self.warehouse = Warehouse(file)

    def run(self):
        warehouse_drawer = WarehouseDrawer(self.warehouse)
        carts = []
        for _ in range(50):
            carts.append(Cart(choice(self.warehouse.starts), self.warehouse))
        warehouse_drawer.carts = carts
        warehouse_drawer.run()


if __name__ == '__main__':
    automated_warehouse = AutomatedWarehouse('wh1.txt')
    automated_warehouse.run()
