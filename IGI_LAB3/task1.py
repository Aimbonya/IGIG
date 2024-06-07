import time
import math


def measure_time(func):
    """ Эта функция используется для вычисления времени выполнения какой либо функции
    func: Принимает функцию
    wrapper: Возвращает время выполнения
    """

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
    for n in range(i):
        result += ((-1) ** n) * ((x ** (2 * n + 1)) / (math.factorial(2 * n + 1)))
    return result


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
        value = sum_function(x, n)
        if abs(sinx - value) < eps or n >= 500:
            break
        else:
            n += 1

    print("x | n | F(x) | Math F(x) | eps")
    print(f"{x} | {n} | {value} | {sinx}| {eps}")


if __name__ == "__main__":
    main()
