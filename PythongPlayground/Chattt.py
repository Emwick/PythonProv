import random

def generate_lotto_numbers():
 num_rows = int(input("Enter the number of rows: "))
 with open("Chattt.txt", "w") as file:
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
def generate_Keno_numbers():
 num_rows = int(input("Enter the number of rows: "))
 with open("Chattt.txt", "w") as file:
  for _ in range(num_rows):

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

    file.write(", ".join(map(str, array)) + "\n")

def generate_EuroJ_numbers():
 num_rows = int(input("Enter the number of rows: "))
 with open("Chattt.txt", "w") as file:
  for _ in range(num_rows):

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

    file.write(", ".join(map(str, array)) + "\n")
    file.write(", ".join(map(str, array2)) + "\n")

def generate_Viking_numbers():
 num_rows = int(input("Enter the number of rows: "))
 with open("Chattt.txt", "w") as file:
  for _ in range(num_rows):

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

    file.write(", ".join(map(str, array)) + "\n")
    file.write(", ".join(map(str, array2)) + "\n")

def display_menu():
    print("Welcome to the Gambling game selector, pick a game 1-4 Number Generator")
    print("1. Generate Lotto Numbers")
    print("2. Generate Keno Numbers")
    print("3. Generate EuroJ Numbers")
    print("3. Generate Viking Numbers")

    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your gambling choice~ : ")
        if choice == '1':
            generate_lotto_numbers()
            print("Lotto numbers generated to Chattt.txt")
        if choice == '2':
          generate_Keno_numbers()
          print("Keno numbers generated to Chattt.txt")
        if choice == '3':
            generate_EuroJ_numbers()
            print("EuroJ numbers generated to Chattt.txt")
        if choice == '4':
            generate_Viking_numbers()
            print("Keno numbers generated to Chattt.txt")

        elif choice == '5':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
