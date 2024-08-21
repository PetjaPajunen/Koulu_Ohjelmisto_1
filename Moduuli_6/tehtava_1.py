import random


def nopanheitto():
    return random.randint(1, 6)


while True:
    noppa = nopanheitto()
    print(noppa)
    if noppa == 6:
        break
