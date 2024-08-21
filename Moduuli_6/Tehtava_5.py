
def segregation(lista):
    new_lista = lista
    for i in new_lista:
        if (i % 2) != 0:
            new_lista.remove(i)
    return (new_lista)


print(segregation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
