class Warehouse:
    def __init__(self, file):
        self.matrix = self.read_file(file)
        for line in self.matrix:
            print(line)

    def read_file(self, file):
        matrix = []

        with open(file, 'r') as f:
            for line in f:
                row = list(line.strip())
                matrix.append(row)

        return matrix

if __name__ == '__main__':
    warehouse = Warehouse('wh1.txt')
