import tkinter as tk

# Функція, яка викликається при натисканні кнопки
def показати_привіт():
    label.config(text="Привіт!")

# Створення головного вікна
window = tk.Tk()
window.title("Кнопка і текст")
window.geometry("300x150")

# Кнопка
button = tk.Button(window, text="Натисни мене", command=показати_привіт)
button.pack(pady=10)

# Мітка, спочатку порожня
label = tk.Label(window, text="", font=("Arial", 16))
label.pack(pady=10)

# Запуск головного циклу
window.mainloop()