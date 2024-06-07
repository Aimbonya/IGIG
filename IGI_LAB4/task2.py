import re


def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def count_sentences(text):
    sentence_regex = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
    sentences = re.split(sentence_regex, text)

    declarative_count = 0
    interrogative_count = 0
    imperative_count = 0

    for sentence in sentences:
        if re.match(r'^[A-ZА-Я].*[\.\?!]$', sentence):
            declarative_count += 1
        elif re.match(r'^[A-ZА-Я].*\?$', sentence):
            interrogative_count += 1
        elif re.match(r'^[A-ZА-Я].*\!$', sentence):
            imperative_count += 1

    return declarative_count, interrogative_count, imperative_count, len(sentences)


def calculate_average_length(text):
    sentences = re.split(r'[.!?]', text)

    total_sentence_length = sum(len(sentence.split()) for sentence in sentences)
    total_sentences = len(sentences)

    words = re.findall(r'\b\w+\b', text)

    total_word_length = sum(len(word) for word in words)
    total_words = len(words)

    average_sentence_length = total_sentence_length / total_sentences if total_sentences > 0 else 0
    average_word_length = total_word_length / total_words if total_words > 0 else 0

    return average_sentence_length, average_word_length


def replace_last_three_chars(text, word_length):
    word_regex = rf'\b\w{{{word_length}}}\b'

    words_to_replace = re.findall(word_regex, text)

    for word in words_to_replace:
        text = text.replace(word, word[:-3] + "$")

    return text


def count_words_with_max_length(text):
    words = re.findall(r'\b\w+\b', text)

    max_word_length = max(len(word) for word in words)

    count_max_length_words = sum(1 for word in words if len(word) == max_word_length)

    return count_max_length_words, max_word_length


def find_words_followed_by_punctuation(text):
    word_punctuation_regex = r'\b\w+\b[,.]'
    words_followed_by_punctuation = re.findall(word_punctuation_regex, text)
    return words_followed_by_punctuation


def find_longest_word_ending_with_e(text):
    words_ending_with_e = re.findall(r'\b\w+е\b', text)

    longest_word = max(words_ending_with_e, key=len)

    return longest_word


def find_time(text):
    time_regex = r'\b\d{2}:\d{2}\b'
    times = re.findall(time_regex, text)
    return times


def count_smileys(text):
    smiley_regex = r'[:;]-*[\(\)\[\]]+'
    smileys = re.findall(smiley_regex, text)

    return len(smileys)


if __name__ == "__main__":
    filetext = read_text_from_file("input.txt")
    maxword_count, maxword_lenght = count_words_with_max_length(filetext)
    av_sent_length, av_word_lenght = calculate_average_length(filetext)
    print(count_sentences(filetext))
    print(round(av_sent_length), round(av_word_lenght))
    print("Количество слов с максимальной длинной: " + str(maxword_count) + "  Длинна: " + str(maxword_lenght))
    print("Количество смайликов: "+str(count_smileys(filetext)))
    print("Самое длинное слово оканчивающееся на е: " + str(find_longest_word_ending_with_e(filetext)))
    print("Слова, за которыми идут знаки препинания: " + str(find_words_followed_by_punctuation(filetext)))


