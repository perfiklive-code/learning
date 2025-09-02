# Задача
# Згенерувати список квадратів чисел від 1 до 20 та вивести його.

mylist = []

for i  in range(1,21):
    mylist.append(i ** 2)
    print(f'Квадрат числа {i} = {mylist[i-1]}')


# Варіант 1 від GPT

squares = [i**2 for i in range(1, 21)]
print(squares)


# Варіант 2 від GPT

mylist = [i ** 2 for i in range(1, 21)]
for i, square in enumerate(mylist, start=1):
        print(f'Квадрат числа {i} = {square}')
        

