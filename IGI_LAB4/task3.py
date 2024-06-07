import time
import math
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполения функции {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper


@measure_time
def sum_function(x, i):
    """Эта функция для вычисления суммы ряда, принимает 2 аргумента:
    x: x
    i: количество итераций
    result: после вычисления возвращает
    """
    result = 0
    values = []
    for n in range(i):
        value = ((-1) ** n) * ((x ** (2 * n + 1)) / (math.factorial(2 * n + 1)))
        result += value
        values.append(value)

    mean = sum(values) / i
    sorted_values = sorted(values)
    if i % 2 == 0:
        median = (sorted_values[i // 2 - 1] + sorted_values[i // 2]) / 2
    else:
        median = sorted_values[i // 2]
    mode = Counter(values).most_common(1)[0][0]
    variance = sum((value - mean) ** 2 for value in values) / i
    standard_deviation = math.sqrt(variance)

    return result, mean, median, mode, variance, standard_deviation, values


def main():
    print("Требуется посчитать функцию при помощи суммы ряда и встроенной функции, получив требуемую точность.")

    bol = 0
    while bol == 0:
        try:
            x = float(input("Введите х:"))
            eps = float(input("Введите точность: "))
            bol = 1
        except ValueError:
            print("Число/несколько чисел были введены неправильно, попробуйте еще раз!")
            bol = 0

    sinx = math.sin(x)
    n = 1

    while True:
        value, av, median, mode, disp, sko, values = sum_function(x, n)
        if abs(sinx - value) < eps or n >= 500:
            break
        else:
            n += 1

    x_values = np.linspace(0, 2 * math.pi, 100)
    y_values = [math.sin(val) for val in x_values]

    # Строим графики
    plt.plot(x_values, y_values, label='sin(x)', color='blue')
    plt.plot(range(1, n + 1), values, label='Series Expansion', color='red')

    # Добавляем заголовок и метки осей
    plt.title('Series Expansion vs sin(x)')
    plt.xlabel('x')
    plt.ylabel('y')

    # Добавляем легенду
    plt.legend()

    # Добавляем текст и аннотацию
    plt.text(0, 0.5, f'Series Expansion: {value}', fontsize=10)
    plt.annotate('sin(x)', xy=(0, 0), xytext=(10, 0.5),
                 arrowprops=dict(facecolor='black', shrink=0.05))

    plt.grid(True)
    plt.show()

    print("x | n | F(x) | Math F(x) | eps")
    print(f"{x} | {n} | {value} | {sinx}| {eps}")


if __name__ == "__main__":
    main()
