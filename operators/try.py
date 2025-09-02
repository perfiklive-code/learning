try:
    num = int(input("Введіть число: "))
    if num % 2 == 0:
        print("Парне")
    else:
        print("Непарне")
except ValueError:
    print("Це не число!")