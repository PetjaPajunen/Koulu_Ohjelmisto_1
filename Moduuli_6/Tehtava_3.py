
def muuntaja(gallon):
    return gallon*3.785


while True:
    gallon = float(input("Gallona: "))
    print(f"{muuntaja(gallon)} Litraa")
    if gallon < 0:
        break
