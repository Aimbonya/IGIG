 # This programm has been developed to make through third lab in IGI. It solves various problems in different tasks.
 # Lab Work N3
 # Lab Theme : "Стандартные типы данных, коллекции, функции, модули."
 # Developer : Mammadov Fakhrat Elshad ogly
 # Date : 30.03.2024


import task1  # Comparison between Math and Sum of Series
import task2  # operations on sequence of numbers
import task3  # Text analysis, amount of punctuation marks
import task4  # Text analysis with split function
import task5  # Work with the list, sum and multiplication

if __name__ == "__main__":

    while True:  # Cycle for UI imitation
        try:
            z = int(input("Введите номер задания, который хотите выполнить(Введите 0 для выхода из программы):"))

            if z == 1:
                task1.main()
            elif z == 2:
                task2.main()
            elif z == 3:
                task3.main()
            elif z == 4:
                task4.main()
            elif z == 5:
                task5.main()
            elif z == 0:
                break
            else:
                print("Вы не выбрали ни один из вариаетов, попробуйье еще раз!(Для завершения программы введите 0)")

        except ValueError:  # Exception for the wrong input
            print("Ошибка: число введено некорректно!")
