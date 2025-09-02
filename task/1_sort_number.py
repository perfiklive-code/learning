"""
Задача: Парні числа до N

Умова:
Напиши програму, яка запитує в користувача число N, а потім виводить усі парні числа від 0 до N (включно).

Приклад вводу:

Введіть число: 10

Приклад виводу:

0 2 4 6 8 10
"""

n = int(input('Введіть число N '))
list = []
for n in range(n+1):
    list.append(n)

even = [x for x in list if x % 2 == 0]

print(even)

# рішення від GPT
n = int(input('Введіть число N: '))
even = [x for x in range(n + 1) if x % 2 == 0]
print(even)