from warehouse import Warehouse
from random import choice
from warehouse_drawer import WarehouseDrawer
from cart import Cart


class AutomatedWarehouse:
    def __init__(self, file):
        self.warehouse = Warehouse(file)
        self.carts = []
        for _ in range(50):
            self.carts.append(Cart(choice(self.warehouse.starts), self.warehouse))

    def run(self):
        warehouse_drawer = WarehouseDrawer(self.warehouse)
        warehouse_drawer.carts = self.carts
        warehouse_drawer.run(self.carts_handling)

    def carts_handling(self):
        for cart in self.carts:
            if not cart.is_path_done():
                cart.move_along_path()

            elif not cart.loaded:
                cart.loaded = True
                new_target = choice(self.warehouse.targets).access_point

                cart.set_path(new_target)
                cart.move_along_path()

            else:
                cart.loaded = False
                new_target = choice(self.warehouse.racks).access_point

                cart.set_path(new_target)
                cart.move_along_path()

if __name__ == '__main__':
    automated_warehouse = AutomatedWarehouse('wh1.txt')
    automated_warehouse.run()
