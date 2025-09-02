import tkinter as tk

# Створення головного вікна
window = tk.Tk()
window.title("Моя програма")
window.geometry("300x100")

# Створення текстової мітки
label = tk.Label(window, text="Привіт, світ!", font=("Arial", 16))

label.pack()

#label.pack(pady=70) # Розміщення по центру з відступом від верху

#label.pack(anchor="nw", padx=10, pady=10)  # Північно-західний кут (лівий верхній) 

#label.place(x=50, y=30)  # Координати в пікселях від верхнього лівого кута

# Запуск головного циклу подій
window.mainloop()