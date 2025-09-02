text = "hello"

print("do", "re", "mi", sep=("___"), end=("!!!"))
print("\n")
print(text.upper()) #все великими літерами
print(text.lower()) #все маленькими літерами
print(text.strip()) # прмбирає  пробіли спереді і ззаді
text = "===Hello==="
print(text.strip("="))  # "Hello"

text.isdigit() #  перевіряє чи  текст складається тільки з цифр

print(f'Привіт, {name}! Через 10 років тобі буде {age + 10}.')

round(число, 2)  # показує кількість знаків після коми

# Не переводить каретку на новий рядок
print("Привіт", end=" ")
print("Світ")   