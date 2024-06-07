 # This programm has been developed to make through third lab in IGI. It solves various problems in different tasks.
 # Lab Work N4
 # Lab Theme : "Работа с файлами, классами, сериализаторами, регулярными выражениями и стандартными библиотеками."
 # Developer : Mammadov Fakhrat Elshad ogly
 # Date : 13.04.2024


import task1
import task2
import task3
import task4
import task5

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
