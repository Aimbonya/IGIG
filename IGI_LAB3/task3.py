import string


def count_punctuation(input_string):  # Functions that counts punctuation marks using string methods
    """Функция для подсчета знаков пунктуации, использует методы встроенного класса string.
    input_string: принимает строку для дальнейшей обработки.
    punctuation_count: возвращает количество символов пунктуации.
    """
    punctuation_count = 0

    for char in input_string:
        if char in string.punctuation:
            punctuation_count += 1

    return punctuation_count


def main():
    print("В строке, вводимой с клавиатуры, подсчитать количество знаков пунктуации")
    user_input = input("Введите строку: ")
    punctuation_count = count_punctuation(user_input)
    print("Количество знаков пунктуации в строке:", punctuation_count)


if __name__ == "__main__":
    main()
