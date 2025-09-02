import tkinter as tk

# Ініціалізація вікна
window = tk.Tk()
window.title("Світлофор")
window.geometry("200x400")
window.resizable(False, False)

# Полотно для малювання світлофора
canvas = tk.Canvas(window, width=200, height=400, bg="gray")
canvas.pack()

# Контур світлофора
canvas.create_rectangle(50, 50, 150, 350, fill="black", outline="white")

# Кола-світлофори
red_light = canvas.create_oval(70, 70, 130, 130, fill="gray")
yellow_light = canvas.create_oval(70, 160, 130, 220, fill="gray")
green_light = canvas.create_oval(70, 250, 130, 310, fill="gray")

# Порядок кольорів
colors = ["red", "yellow", "green"]
index = 0

def change_light():
    global index
    # Гасимо всі
    canvas.itemconfig(red_light, fill="gray")
    canvas.itemconfig(yellow_light, fill="gray")
    canvas.itemconfig(green_light, fill="gray")

    # Вмикаємо відповідний колір
    current_color = colors[index]
    if current_color == "red":
        canvas.itemconfig(red_light, fill="red")
    elif current_color == "yellow":
        canvas.itemconfig(yellow_light, fill="yellow")
    elif current_color == "green":
        canvas.itemconfig(green_light, fill="green")

    # Переходимо до наступного кольору
    index = (index + 1) % len(colors)

    # Повторити через 2 секунди (2000 мс)
    window.after(2000, change_light)

# Запуск анімації
change_light()

# Головний цикл
window.mainloop()