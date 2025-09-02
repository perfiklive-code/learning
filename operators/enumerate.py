fruits = ["яблуко", "груша", "слива"]

e = enumerate(fruits)  # створюємо enumerate-об'єкт
print(list(e))         # перетворимо в список пар (індекс, значення)

fruit_dict = dict(enumerate(fruits, start=1))
print(fruit_dict) # start = 1 починаємо нумерацію з 1



for index, value in enumerate(fruits):
    print(index, value)
