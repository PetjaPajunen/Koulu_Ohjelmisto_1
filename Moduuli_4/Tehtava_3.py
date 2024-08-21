
lista = []

while True:
    num = input("Anna luku: ")
    if num == "":
        print(f"Pienin numero: {min(lista)}    Suurin numero: {max(lista)}")
        break
    lista.append(int(num))
