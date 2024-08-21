
kayttaja = "A.A"
salasana = "AA"

while True:
    kKayttaja = input("Käyttäjä tunnus: ")
    kSalasana = input("Salasana: ")

    if kKayttaja != kayttaja or salasana != kSalasana:
        print("Pääsy evätty. ")
        continue

    print("Tervettuloa. ")
    break
