
lista = []

while True:
    num = input("Anna kokonaisluku: ")

    if num == "":
        lista.sort(reverse=True)
        print(f"5 Suurinta lukua: {lista[:5]}")
        break
    lista.append(int(num))
