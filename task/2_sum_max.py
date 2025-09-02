'''
Задача:
Напиши програму, яка запитує у користувача три числа, а потім виводить:

Найбільше з них.

Середнє арифметичне всіх трьох чисел.
'''

number = [int(input('Введи 1 число: '))]
number += [int(input('Введи 2 число: '))]
number += [int(input('Введи 3 число: '))]

max = int()
sum = float()

for i in range(len(number)):
		if max < number[i]:
			max = number[i]

for i in range(len(number)):
			sum += number[i]

sum = sum / len(number)

print(f'Найбільше число: {max}')
print(f'Середнє арифметичне: {round(sum, 2)}')


#Рішення від GPT:

number = []

# Вводимо три числа
for i in range(1, 4):
    n = int(input(f'Введи {i} число: '))
    number.append(n)

max_value = max(number)
avg = sum(number) / len(number)

print(f'Найбільше число: {max_value}')
print(f'Середнє арифметичне: {round(avg, 2)}')

