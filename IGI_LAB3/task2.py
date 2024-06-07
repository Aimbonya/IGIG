def count_even_numbers():  # Function for counting even numbers
    """"Функция для подсчета четных чисел, ввод оформлен внутри
    count: Возвращает количество четных натурильных чисел
    """
    count = 0

    while True:
        try:
            num = int(input("Введите целое число (Введите 0 для завершения): "))  # Input in cycle while getting 0
            if num == 0:
                break
            elif num % 2 == 0 and num > 0:
                count += 1
        except ValueError:
            print("Число введено неправильно!")
    return count


def main():
    print("Организовать цикл, который принимает целые числа и вычисляет количество четных натуральных чисел.\n Окончание – ввод 0\n\n")
    even_count = count_even_numbers()
    print("Количество четных натуральных чисел:", even_count)


if __name__ == "__main__":
    main()