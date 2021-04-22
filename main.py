import re

print('This is the final lesson from regular expression')

all_apes = re.findall("ape", "The ape was in the apex")

for i in all_apes:
    print(i)