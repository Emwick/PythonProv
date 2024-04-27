import random

array = []
seen = set()
for i in range(1, 11):
    num = random.randrange(i, 70)
    while num in seen:
        num = random.randrange(i, 70)
    seen.add(num)
    array.append(num)

array.sort()
print(array)

with open("Keno.txt", "w") as file:
    for number in array:
        file.write(str(number) + ", ")
