import inputTask5


def find_max_min_indices(numbers):  # function that finds maximum and minimum indexes
    """Функция для нахождения индексов максимального и минимальных значений
    Return: возвращает индексы миниммума и максимума значений
    """
    max_index = numbers.index(max(numbers, key=abs))
    min_index = numbers.index(min(numbers, key=abs))
    return min(max_index, min_index), max(max_index, min_index)


def sum_non_negative_elements(numbers):
    return sum(num for num in numbers if num >= 0)


def product_between_indices(numbers, start, end):  # Function that returns multiply between max and min
    """Функция для нахождения произведения значений между максимумом и минимумом.
    numbers,start, end: Принимает список, ондекс минимума и максимума и минимума
    далее проходится от максимума до минимума, перемножая все значения и сохраняя результат в product
    product: возвращает произведение всех значений.
    """
    if start >= end:
        return 0

    product = 1
    for num in numbers[start + 1:end]:
        product *= num
    return product


def main():
    print("Программа для обработки вещественных списков.")

    while True:
        try:
            l = int(input("Выберите метод ввода списков: 1- рандомная генерация списка/2-ввод списка вручную:"))
            if l == 2:
                numbers = inputTask5.input_list()
                break
            elif l == 1:
                numbers = list(inputTask5.generate_random())
                break
        except ValueError:
            print("Число введено некорректно! Попробуйте еще раз!")

    if not numbers:
        print("Ошибка: Список пуст.")
    else:
        non_negative_sum = sum_non_negative_elements(numbers)
        min_index, max_index = find_max_min_indices(numbers)
        product = product_between_indices(numbers, min_index, max_index)

        print("Сумма неотрицательных элементов:", non_negative_sum)
        print("Произведение элементов списка между максимальным и минимальным по модулю элементами:", product)

        print("Список:", numbers)


if __name__ == "__main__":
    main()
