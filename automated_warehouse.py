from warehouse import Warehouse


class AutomatedWarehouse:
    def __init__(self, file):
        self.warehouse = Warehouse(file)

    def run(self):
        pass


if __name__ == '__main__':
    automated_warehouse = AutomatedWarehouse('wh1.txt')
    automated_warehouse.run()
