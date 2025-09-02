from datetime import date

class Dog:
    def __init__(self, name, age):
        """Базовий конструктор"""
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Конструктор з року народження"""
        age = date.today().year - birth_year
        return cls(name, age)

    @classmethod
    def unnamed(cls, age):
        """Конструктор для безіменної собаки"""
        return cls("Безіменний", age)

    def __str__(self):
        return f"Собака {self.name}, {self.age} років"

# --- Приклади створення об'єктів ---
dog1 = Dog("Лаврик", 5)               # Звичайний конструктор
dog2 = Dog.from_birth_year("Барбос", 2020)  # З року народження
dog3 = Dog.unnamed(2)                 # Безіменна собака

print(dog1)
print(dog2)
print(dog3)