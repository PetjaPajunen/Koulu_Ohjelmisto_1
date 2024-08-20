
def hytit():
    luokka = input("Hytti luokka: ")

    if luokka == "LUX".lower():
        print("LUX on parvekkeellinen hytti yläkannella")
    elif luokka == "A".lower():
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    elif luokka == "B".lower():
        print("B on ikkunaton hytti autokannen yläpuolella.")
    elif luokka == "C":
        print("C on ikkunaton hytti autokannen alapuolella.")
    else:
        print("Virheellinen hyttiluokka")


hytit()
