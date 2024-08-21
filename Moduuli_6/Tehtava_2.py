import random


def nopanheitto(tahko):
    return random.randint(1, tahko)


tahko = int(input("Tahko: "))
while True:
    noppa = nopanheitto(tahko)
    print(noppa)
    if noppa == tahko:
        break
