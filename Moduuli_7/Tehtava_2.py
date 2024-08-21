
sets = set({})

while True:
    name = input("Anna nimi: ")
    if name == "":
        for i in sets:
            print(i)
        break

    if name not in sets:
        print("New name.")
        sets.add(name)
    elif name in sets:
        print("Existing name.")
