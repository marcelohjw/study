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