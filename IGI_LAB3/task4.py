def count_consonant_ending_words(text):  # Function that checks consonant ending
    """Функция для проверки окончания слова
    text: принимает строку для дальнейшей обработки
    при помощи создания строки состоящей из гласных букв проверяет на совпадения последние символы
    constant_ending_count: возвращает количсетво найденных символов
    """
    vowels = 'aeiouAEIOU'  # Initializing vowels
    consonant_ending_count = 0

    words = text.split()
    for word in words:
        if not word[-1].isalpha():
            if word[-2] not in vowels:  # checking if last symbol is punc symb, if it is checks [-2]
                consonant_ending_count += 1
        else:
            if word[-1] not in vowels:  # Checking if last symbol is consonant
                consonant_ending_count += 1

    return consonant_ending_count


def average_length_words(text):  # Function that checks words length
    """Функция для расчета средней длины слов и нахождения слов данной длинны
    text: принимает строку для дальнейшей обработки
    после получения строки делит ее на слова и обрабатывает
    average length, words_of_length: возвращает среднюю длинну и список из слов данной длинны
    """
    words = text.split()  # Splitting text in words and putting them in words list
    total_length = sum(len(word) for word in words)
    num_words = len(words)

    if num_words == 0:
        return None

    average_length = total_length // num_words

    words_of_length = [word for word in words if len(word) == average_length]

    return average_length, words_of_length


def every_seventh_word(text):  # Every seventh word function
    """Функция для создания списка из каждого седьмого слова
    text: принимает строку для дальнейшей обработки
    далее тект делится на слова и каждое седьмое слово добавляется в список
    seventh_word: возвращает список содержащий каждое седьмое слово текста
    """
    words = text.split()
    seventh_words = [word for index, word in enumerate(words) if (index + 1) % 7 == 0]

    return seventh_words


def main():
    input_text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."

    print("Дана строка текста, в которой слова разделены пробелами и запятыми. В соответствии с заданием своего варианта составьте программу для анализа строки, инициализированной в коде программы")
    print("Число слов, заканчивающихся на согласную:", count_consonant_ending_words(input_text))

    result = average_length_words(input_text)
    if result is not None:
        average_length, words_of_length = result
        if len(words_of_length) > 0:
            print(f"Средняя длина слов в строке: {average_length}")
            print("Слова с такой длиной:", words_of_length)
        else:
            print(f"Слов длиной {average_length} символов в строке нет")
    else:
        print("В строке нет слов")

    seventh_words = every_seventh_word(input_text)
    print("Каждое седьмое слово:", seventh_words)


if __name__ == "__main__":
    main()
