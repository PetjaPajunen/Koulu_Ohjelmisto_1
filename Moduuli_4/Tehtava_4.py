import random
num = random.randint(1, 10)

while True:
    guess = int(input("Anna kokonaisluku: "))

    if num == guess:
        print("Oikein.")
        break
    elif num > guess:
        print("Liian pieni.")
    elif num < guess:
        print("Liian suuri.")
