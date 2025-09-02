import random

random.randint(від, до)

fruits = ['яблуко', 'банан', 'слива']
print(random.choice(fruits)) #випадкове значення зі списку

print(random.sample(fruits, 2)) # вибирає 2 випадкових елемента без повторень

print(random.choices(fruits, k=4)) # вибирає к елементів з повтореннями


cards = ['туз', 'король', 'дама', 'валет']
random.shuffle(cards)  # перемішує список

print(random.uniform(1.0, 5.0))  # Наприклад: 2.738

print(random.choice(['Орел', 'Решка']))

