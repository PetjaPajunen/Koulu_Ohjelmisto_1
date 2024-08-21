
seasons = ("spring", "summer", "autumn", "winter")

month = int(input("Kuukausi: "))

if month == 12 or month == 1 or month == 2:
    print(seasons[3])
elif month > 2 and month < 6:
    print(seasons[0])
elif month > 5 and month < 9:
    print(seasons[1])
elif month > 9 and month < 12:
    print(seasons[2])
