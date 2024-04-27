import random


num_rows = int(input("Enter the number of rows: "))
with open("Test.txt", "w") as file:
 for _ in range(num_rows):

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

    file.write(", ".join(map(str, array)) + "\n")