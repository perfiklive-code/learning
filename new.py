def print_triangle_with_exclamation(height: int, fill: str = "*") -> None:
    """
    Друкує рівнобедрений трикутник із символів fill.
    У центрі розташовується знак оклику (!).
    """
    if height < 2:
        print("Висота має бути >= 2")
        return

    for i in range(1, height + 1):
        # формуємо рядок з заповнювача
        line = fill * (2 * i - 1)
        # позиція центру
        center = len(line) // 2

        if i == height // 2 + 1:  # приблизно середина трикутника
            line = line[:center] + "!" + line[center + 1:]

        # додаємо відступи для центрування
        print(" " * (height - i) + line)


if __name__ == "__main__":
    print_triangle_with_exclamation(9, "#")
