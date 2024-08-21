
num = int(input("Anna kokonaisluku: "))

if num <= 1:
    print("Ei ole alkuluku. ")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("Ei ole alkuluku. ")
            break
        else:
            print("Alkuluku. ")
            break
