leivistkä = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

luoti_gramma = 13.3
naula_gramma = 13.3 * 32
leivistkä_gramma = naula_gramma * 20

luoti_paino = luoti * luoti_gramma
naula_paino = naulat * naula_gramma
leivistkä_paino = leivistkä * leivistkä_gramma


summa = leivistkä_paino + naula_paino + luoti_paino

print(f"{int(summa / 1000)} kilogrammaa ja {round(float(summa % 1000), 2)} grammaa.")