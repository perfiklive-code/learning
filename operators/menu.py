import readchar

menu_items = ["Привітати", "Порахувати суму двох чисел", "Вийти"]

# ANSI-коди для кольорів
COLOR_ACTIVE = "\033[92m"  # Зелений
COLOR_RESET = "\033[0m"    # Скидання кольору

def print_menu(selected_index):
    print("\n=== Меню ===")
    for i, item in enumerate(menu_items):
        if i == selected_index:
            print(f"{COLOR_ACTIVE}> {item}{COLOR_RESET}")  # Підсвічений активний пункт
        else:
            print(f"  {item}")

def interactive_menu():
    selected = 0
    while True:
        # Очищуємо консоль
        print("\033c", end="")
        print_menu(selected)

        # Читаємо натиснуту клавішу
        key = readchar.readkey()

        if key == readchar.key.UP:
            selected = (selected - 1) % len(menu_items)
        elif key == readchar.key.DOWN:
            selected = (selected + 1) % len(menu_items)
        elif key == readchar.key.ENTER:
            print("\033c", end="")  # Очищаємо консоль перед дією
            if selected == 0:
                print("Привіт! Гарного дня!")
                input("\nНатисніть Enter для повернення до меню...")
            elif selected == 1:
                try:
                    a = float(input("Введіть перше число: "))
                    b = float(input("Введіть друге число: "))
                    print(f"Сума: {a + b}")
                except ValueError:
                    print("Будь ласка, введіть числа!")
                input("\nНатисніть Enter для повернення до меню...")
            elif selected == 2:
                print("До побачення!")
                break

interactive_menu()
