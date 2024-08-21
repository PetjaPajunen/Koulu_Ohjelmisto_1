import random

arpa = 6
lista = []
pituus = int(input("Anna kokonaislukuna arpojen määrä: "))

for i in range(pituus):
    num = random.randint(1, 6)
    lista.append(num)

print(sum(lista))
