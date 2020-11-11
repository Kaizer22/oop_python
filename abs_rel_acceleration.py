"""
*Дополнительное задание вне курса*
Функция, получающая на вход плоский список целочисленных
значений или значений с плавающей точкой
В качестве результата возвращает список из двух списков - абсолютное ускорение и
отностительное ускорение:
[[absolute_acceleration],[relative_acceleration]]

По опеделению имеем:
Абсолютное ускорение - разница между абсолютным приростом
за данный период и абсолютным приростом за предыдущий период равной длительности.
Измеряется только цепным способом.
Относительное ускорение - отношение цепного темпа прироста за данный период и
цепного темпа за предыдущий период

"""


def find_accelerations(numbers):
    # Проверка того, что полученное значение - список
    if isinstance(numbers, list):
        # Проверим, что список является плоским и содержит целочисленные значения
        # или значения с плавающей точкой
        for i in numbers:
            if (not isinstance(i, int)) and (not isinstance(i, float)):
                # Иначе, сообщим пользователю о некорректном вводе и вернем пустые списки
                print("find_acceleration() : Введены некорректные значения! Требуется передать в функцию"
                      "плоский список int или float.")
                return [], []
        # Цепной абсолютный прирост и цепной темп прироста
        absolute_growth = list()
        relative_growth_rate = list()

        # Абсолютное и относительное ускорения
        absolute_acceleration = list()
        relative_acceleration = list()

        # Расчет цепного абсолютного прироста и цепного темпа прироста
        for i in range(1, len(numbers)):
            absolute_growth.append(numbers[i] - numbers[i - 1])
            relative_growth_rate.append(absolute_growth[i - 1] / numbers[i - 1])

        # Расчет цепных абсолютных и относительных ускорений
        for i in range(1, len(absolute_growth)):
            absolute_acceleration.append(absolute_growth[i] - absolute_growth[i - 1])
            relative_acceleration.append(relative_growth_rate[i] / relative_growth_rate[i - 1])

        # Для отладки и тестирования
        # print(absolute_growth)
        # print(relative_growth_rate)
        return absolute_acceleration, relative_acceleration
    else:
        # Иначе, сообщим пользователю о некорректном вводе и вернем пустые списки
        print("find_acceleration() : Введены некорректные значения! Требуется передать в функцию"
              " плоский список int или float.")
        return [], []


# Тестовые значения временного ряда
test1 = ["dssf", 10, 12, 21, 2, 212, 2, 1]
test2 = [[1,2,3,4],2,4,5,6]
test3 = [1,3,5,6,34,5,2,12,45,43,7,100,12]
test4 = [1,100,150]
absolute_acceleration_res, relative_acceleration_res = find_accelerations(test1)
print(absolute_acceleration_res)
print(relative_acceleration_res)
absolute_acceleration_res, relative_acceleration_res = find_accelerations(test2)
print(absolute_acceleration_res)
print(relative_acceleration_res)
absolute_acceleration_res, relative_acceleration_res = find_accelerations(test3)
print(absolute_acceleration_res)
print(relative_acceleration_res)
absolute_acceleration_res, relative_acceleration_res = find_accelerations(test4)
print(absolute_acceleration_res)
print(relative_acceleration_res)
