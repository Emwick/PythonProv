import random


array = []
seen = set()
for i in range(1, 8):
    num = random.randrange(i, 40)
    while num in seen:
        num = random.randrange(i, 40)
    seen.add(num)
    array.append(num)

array.sort()
print(array)
