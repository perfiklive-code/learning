'''
Задача:
Напиши програму, яка приймає список чисел і повертає новий список, де залишаються тільки парні числа, помножені на 2.

Приклад:
Вхід: [1, 2, 3, 4, 5, 6]
Вихід: [4, 8, 12]
'''


# Введення рядка чисел через пробіл
input_str = input("Введіть числа через пробіл: ")

# Розбиваємо рядок на окремі елементи (рядки)
str_numbers = input_str.split()

# Перетворюємо кожен елемент у ціле число
my_list = [int(num) for num in str_numbers]

sort_list = []

for i in range(len(my_list)):
	if my_list[i] % 2 == 0:
		sort_list.append(my_list[i]*2)


print(sort_list)



###Рішення від GPT

input_str = input("Введіть числа через пробіл: ")
my_list = [int(num) for num in input_str.split()]

sort_list = [x * 2 for x in my_list if x % 2 == 0]

print(sort_list)