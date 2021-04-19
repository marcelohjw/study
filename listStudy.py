import random

print("Here i study list of comprehensions")

print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])

multi_list = [[1, 2, 3],
              [4, 5, 6],
              [7, 99, 10]]

print([col[1] for col in multi_list])


# Generator Stuff

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
        return True


def gen_prime(max_number):
    for num1 in range(2, max_number):
        if is_prime(num1):
            yield num1


prime = gen_prime(50)
print("Prime:", next(prime))
print("Prime:", next(prime))
print("-----------------")
doubles = (x * 2 for x in range(10))
for i in doubles:
    print("Double:", next(doubles))