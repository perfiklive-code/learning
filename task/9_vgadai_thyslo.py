
import random
import os # для очищення терміналу
import readchar # для меню

menu_items = ["Початок гри", "Налаштування ліміту", "Вийти"]

def print_menu(selected_index):
    print_banner()
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

    def reset(self):
        self.low = 1
        self.high = 100

# Кольори
DARK_GREEN = "\033[32m"  # темно зелений
TURQUOISE = "\033[36m"   # бірюзовий
GREEN = "\033[92m"       # Зелений
RESET = "\033[0m"        # сірий - стандартний

limit = Limits()

money = 0

while True:

    match interactive_menu():
        case 1:
            limit.manual()
        case 2:
            print('Гру закінчено!')
            break

    count = 1
    status = '\nСпробуй свою удачу!\n'
    sicret_value = random.randint(limit.low, limit.high)

    clear_console()

    while True:

        print_banner()
        print(f'Ваш баланс: {money}$')
        print(f'Спроба: {count}')
        print(status)
        user_value = input(f'Введіть число від {limit.low} до {limit.high}  \n')

        clear_console()

        match user_value.strip().lower():

            case 'n':
                print('Ви здалися!')
                limit.reset()
                break

            case 'd':
                debug = True
                print(DARK_GREEN + f"Відповідь: {sicret_value}\n" + RESET)
                continue

            case _ :
                user_value = to_int(user_value)

        match user_value:

            case n if n == sicret_value:
                print(f'Вітаю ви виграли за {count} спроб(и)!!!\n')
                money += 10
                limit.reset()
                input()
                break

            case n if n < sicret_value:
                if user_value < limit.low:
                    status = '\nВи що смієтесь, це навіть менше ніж ліміт!\n'
                else:
                    status = '\nВи не вгадали, необхідно ввести БІЛЬШЕ значення\n'

            case n if n > sicret_value:
                if user_value > limit.high:
                    status = '\nВи що смієтесь, це навіть більше за ліміт!\n'
                else:
                    status = '\nВи не вгадали, необхідно ввести МЕНШЕ значення\n'

        count += 1

        limit.correct(user_value, sicret_value)
