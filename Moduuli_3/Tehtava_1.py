
def mittaus():
    kalanPituus = float(input("Kalan mitta: "))

    if kalanPituus > 37:
        return
    print(f"Laske kuha takaisin {37-kalanPituus}cm liian lyhyt")


mittaus()
