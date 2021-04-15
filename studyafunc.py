from functools import reduce
import random

choice = ["h", "t"]
ht_list = []

i = 0
while i < 50:
    i += 1
    pick = random.choice(choice)
    ht_list.append(pick)

h_list = []
t_list = []
for c in ht_list:
    if c == "h":
        h_list.append(c)
    elif c == "t":
        t_list.append(c)

print("Heads:", len(h_list))
print("Tails:", len(t_list))

# Map uses
one_to_10 = range(1, 11)


def dbl_num(num):
    return num * 2


print("MAP")
print(list(map(dbl_num, one_to_10)))

# Filter uses
print("FILTER")

rand_list = list(random.randint(1, 1001) for i in range(100))
print(list(filter((lambda x: x % 9 == 0),
                  rand_list)))
print("EVEN FILTER TRY")
even_list_try = list(range(1, 11))
print(list(filter((lambda x: x % 2 == 0), even_list_try)))

# Reduce use
print("REDUCE")
print(reduce((lambda x, y: x + y), range(1, 6)))
