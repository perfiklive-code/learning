'''
Завдання:
Напиши програму, яка запитує в користувача число та визначає, чи є воно простим.

Просте число — це число більше 1, яке ділиться тільки на 1 і на себе.
'''
number = float(input('Введіть ваше число: '))

if number < 2 or number != int(number):
    print("Число має бути цілим і більшим за 1")
else:
    number = int(number)
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            print('Число складене')
            is_prime = False
            break

    if is_prime:
        print('Число просте')
        
# Варіант GPT

while True:
    user_input = input("Введіть ціле число більше за 1 (або 'вихід' для завершення): ")

    if user_input.lower() == 'вихід':
        print("Завершення програми.")
        break

    if not user_input.isdigit():
        print("Помилка: введено не число.")
        continue

    number = int(user_input)

    if number < 2:
        print("Число має бути більше за 1.")
        continue

    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):  # Досить перевірити до кореня з числа
        if number % i == 0:
            print("Число складене")
            is_prime = False
            break

    if is_prime:
        print("Число просте")
	