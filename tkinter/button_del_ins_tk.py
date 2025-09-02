import tkinter as tk

def move_button(num):
    match num:
        case 1:
            button5.place_forget()
        case 2:
            button6.place_forget()
        case 3:
            button5.place(x=750, y=50)
        case 4:
            button6.place(x=750, y=200)

# Створення головного вікна
window = tk.Tk()
window.title("Кнопка, що зникає")
window.geometry("300x300")

# Створення кнопок з правильним викликом функції
button1 = tk.Button(window, text="Сховати", command=lambda: move_button(1))
button1.place(x=50, y=50)

button2 = tk.Button(window, text="Сховати", command=lambda: move_button(2))
button2.place(x=50, y=200)

button3 = tk.Button(window, text="Показати", command=lambda: move_button(3))
button3.place(x=400, y=50)

button4 = tk.Button(window, text="Показати", command=lambda: move_button(4))
button4.place(x=400, y=200)

button5 = tk.Button(window, text="X")
button5.place(x=750, y=50)

button6 = tk.Button(window, text="X")
button6.place(x=750, y=200)

# Запуск головного циклу
window.mainloop()