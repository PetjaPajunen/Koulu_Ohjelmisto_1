
sukupuoli = input("Sukupuoli: ")
hemo = int(input("hemoglobiiniarvon (g/l): "))


def mies(hemost):
    if hemost > 195:
        print("Korkea")
    elif hemost < 134:
        print("Alhainen")
    else:
        print("Normaali")


def nainen(hemost):
    if hemost > 175:
        print("Korkea")
    elif hemost < 117:
        print("Alhainen")
    else:
        print("Normaali")


if sukupuoli == "mies" or sukupuoli == "m":
    mies(hemo)
elif sukupuoli == "nainen" or sukupuoli == "n":
    nainen(hemo)
