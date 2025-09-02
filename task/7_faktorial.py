### Задача
# Знайдіть факторіал числа

n = input('Введіть число для знаходження його факторіалу: ')

if n.isdigit():
    num = int(n)
    fak = 1
    for i in range(1, num + 1):
        fak *= i
    print(f'Факторіал числа {num} = {fak}')
else:
    print('Це не число!')
    
    
#Варіант 1 GPT

print(__import__("math").factorial(int(input("Введіть число: "))))

#Варіант 2 GPT

n = input("Введіть число: "); print(__import__("math").factorial(int(n))) if n.isdigit() else print("Це не число!")

#Варіант 3 GPT

print(eval('*'.join(str(i) for i in range(1, int(input("Введіть число: ")) + 1)) or "1"))

#Варіант 4 GPT

from functools import reduce; print(reduce(lambda x, y: x * y, range(1, int(input("Введіть число: ")) + 1), 1))