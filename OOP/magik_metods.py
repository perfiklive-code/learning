class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tricks = []

    # Людяне представлення
    def __str__(self):
        return f"Собака {self.name}, {self.age} років"

    # Представлення для розробника
    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age!r})"

    # Довжина об’єкта (кількість трюків)
    def __len__(self):
        return len(self.tricks)

    # Додаємо трюк через індексацію
    def __setitem__(self, index, trick):
        if index == len(self.tricks):  # Додаємо новий трюк
            self.tricks.append(trick)
        else:  # Змінюємо існуючий
            self.tricks[index] = trick

    # Отримуємо трюк за індексом
    def __getitem__(self, index):
        return self.tricks[index]

    # Порівняння собак за віком
    def __gt__(self, other):
        return self.age > other.age

    # Виклик об’єкта як функції
    def __call__(self, sound="Гав!"):
        return f"{self.name} каже: {sound}"


# --- Приклади використання ---
dog1 = Dog("Лаврик", 5)
dog2 = Dog("Барбос", 3)

print(dog1)            # __str__
print(repr(dog1))      # __repr__

dog1[0] = "Сидіти"     # __setitem__
dog1[1] = "Лежати"
print(dog1[0])         # __getitem__
print(len(dog1))       # __len__

print(dog1 > dog2)     # __gt__

print(dog1("Гав-Гав")) # __call__