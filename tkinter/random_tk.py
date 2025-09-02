import tkinter as tk
import random

def generate_number():
    number = random.randint(1, 100)
    result_label.config(text=f"Випадкове число: {number}")

# Створення головного вікна
window = tk.Tk()
window.title("Генератор випадкових чисел")
window.geometry("300x150")

# Контейнер для центрованого розташування
frame = tk.Frame(window)
frame.pack(expand=True)

# Кнопка по центру
generate_button = tk.Button(frame, text="Згенерувати число", command=generate_number)
generate_button.pack(pady=10)

# Мітка для результату
result_label = tk.Label(frame, text="Натисни кнопку")
result_label.pack(pady=10)

# Запуск GUI
window.mainloop()#