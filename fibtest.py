class Fib_Generator:
    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib_num = self.first + self.second
        self.first = self.second
        self.second = fib_num
        return fib_num


fib_seq = Fib_Generator()

for i in range(10):
    print("Fib :", next(fib_seq))
