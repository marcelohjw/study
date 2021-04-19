import random

print("Here i study list of comprehensions")

print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])

multi_list = [[1, 2, 3],
              [4, 5, 6],
              [7, 99, 10]]

print([col[1] for col in multi_list])