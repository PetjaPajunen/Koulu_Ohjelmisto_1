
airDic = {}

while True:
    option = input("Choose action: ")

    if option.lower() == "quit":
        print("Turning off.")
        break

    elif option.lower() == "enter":
        icao = input("ICAO: ")
        airport = input("Name: ")
        airDic[icao.lower()] = airport

    elif option.lower() == "fetch":
        icao = input("ICAO: ")
        print(f"Airport name: {airDic[icao]}")
