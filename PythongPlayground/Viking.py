import random

array = []
seen = set()
for i in range(1, 7):
    num = random.randrange(i, 48)
    while num in seen:
        num = random.randrange(i, 48)
    seen.add(num)
    array.append(num)
array.sort()
print("Första sex")
print(array)

array2 = [random.randint(1, 5) for _ in range(1)]
print("Plus den ena")
print(array2)

with open("Viking.txt", "w") as file:
    for number in array:
        file.write(str(number) + ", ")