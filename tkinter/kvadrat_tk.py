import tkinter as tk

def calculate_square():
    try:
        number = float(entry.get())
        result = number ** 2
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Будь ласка, введіть коректне число")

# Створюємо головне вікно
window = tk.Tk()
window.title("Квадрат числа")
window.geometry("300x150")

# Поле вводу
entry = tk.Entry(window)
entry.pack(pady=10)

# Кнопка
button = tk.Button(window, text="Піднести до квадрату", command=calculate_square)
button.pack()

# Мітка для виводу результату
result_label = tk.Label(window, text="Результат:")
result_label.pack(pady=10)

# Запуск GUI
window.mainloop()