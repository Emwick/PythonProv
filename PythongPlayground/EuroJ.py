import random

array = []
seen = set()
for i in range(1, 6):
    num = random.randrange(i, 50)
    while num in seen:
        num = random.randrange(i, 50)
    seen.add(num)
    array.append(num)
array.sort()
print("Första fem")
print(array)

array2 = [random.randint(1, 12) for _ in range(2)]
print("Plus de två")
print(array2)

with open("EuroJ.txt", "w") as file:
    for number in array:
        file.write(str(number) + ", ")