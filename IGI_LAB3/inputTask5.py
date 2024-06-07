import random


def input_list():  # input function with exceptions
    """Функция для ввода с проверкой элементов на правильность ввода
    elements: возвращает список состоящий из вещественных чисел
    """
    while True:
        try:
            num = int(input("Введите размер списка: "))
            elements = []
            while len(elements) < num:
                element = float(input(f"Введите элемент {len(elements)+1} списка: "))
                elements.append(element)
            return elements
        except ValueError:
            print("Ошибка: Введите числа корректно.")


def generate_random():
    """Генератор для случайной генерации случайных значений."""
    while True:
        try:
            num = int(input("Введите размер списка: "))
            break
        except ValueError:
            print("Ошибка: Введите число корректно.")

    for _ in range(num):
        yield random.uniform(-100.0, 100.0)
