
import random
import os # для очищення терміналу
import readchar # для меню

menu_items = ["Початок гри", "Налаштування ліміту", "Вийти"]

def print_menu(selected_index):
    print("\n=== Меню ===")
    for i, item in enumerate(menu_items):
        if i == selected_index:
            print(f"{GREEN}> {item}{RESET}")  # Підсвічений активний пункт
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
            break
    return selected

    # Заставка
def print_banner():

    banner_ascii = r"""
  ██████╗  ███╗   ██╗
 ██╔═══  ╗ ████╗  ██║
 ██║   ██║ ██╔██╗ ██║
 ██║    █║ ██║╚██╗██║
 ╚██████╔╝ ██║ ╚████║
  ╚═════╝  ╚═╝  ╚═══╝
    """
    print(TURQUOISE + banner_ascii + RESET)
    print('[N] - Вихід     [S] - Суперкористувач\n')

# Очистка консолі
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

    # конвертація в int з перевіркою
def to_int(value: str) -> int:
    while True:
        try:
            return int(value)
        except ValueError:
            value = input('Це не ціле число! Введіть значення ще раз ')

class Limits:
    def __init__(self):
        self.low = 1
        self.high = 100

    def correct(self, user, random_val):
        if self.low < user < random_val:
            self.low = user
        elif random_val < user < self.high:
            self.high = user

    def manual(self):
        print('Ви в режимі суперкористувача')
        self.low = to_int(input('Введіть нижній діапазон: '))
        while True:
            self.high = to_int(input('Введіть верхній діапазон: '))
            if self.high > self.low:
                clear_console()
                break
            else:
                print('Помилка, верхній діапазон повинен бути більшими за нижній!')

# Кольори
DARK_GREEN = "\033[32m" # темно зелений
TURQUOISE = "\033[36m"    # бірюзовий
GREEN = "\033[92m"      # Зелений
RESET = "\033[0m"                 # сірий - стандартний

limit = Limits()

to_close = True
super_user = False
win = False

#print(interactive_menu())

while to_close:
    count = 1
    debug = False

    sicret_value = random.randint(limit.low, limit.high)
    super_user = False

    if count == 1 and not win:
        print_banner()
        win = False

    while True:
        if interactive_menu() == 1:
            limit.manual()


        print(f'Спроба: {count}')
        user_value = input(f'Введіть число від {limit.low} до {limit.high}  \n')

        clear_console()
        print_banner()


        match user_value.strip().lower():
                case 'n':
                        print('Гру закінчено!')
                        to_close = False
                        break

                case 'd':
                        debug = True
                        print(DARK_GREEN + f"Відповідь: {sicret_value}\n" + RESET)
                        continue

                case 's':
                        limit.manual()
                        win = False
                        break

                case _:
                        user_value = to_int(user_value)
        match user_value:
            case n if n == sicret_value:
                print(f'Вітаю ви виграли за {count} спроб(и)!!!\n')
                win = True
                break

            case n if n < sicret_value:
                if user_value < limit.low:
                    print('Ви що смієтесь, це навіть менше ніж ліміт!')
                print('Ви не вгадали, необхідно ввести БІЛЬШЕ значення\n')

            case n if n > sicret_value:
                if user_value > limit.high:
                    print('Ви що смієтесь, це навіть більше за ліміт!' )
                print('Ви не вгадали, необхідно ввести МЕНШЕ значення\n')


        count += 1

        limit.correct(user_value, sicret_value)


