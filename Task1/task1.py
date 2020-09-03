# Инициализация величин и списка

# Константные величины вынесены в начало для
# удобства их редактирования
DEFAULT_TASK_CONSTANT = 0.13
DEFAULT_OUTPUT_FILE = "output.txt"
DEFAULT_IS_DECREMENT_ORDER = False

# Основной список всех значений
task_list = list()


# Получение следующего значения из потока ввода
# Проверка корректности ввода, в случае некоректного ввода возвращается
# флаг, который препятсвует добавлению элемента в список
# Проверка наличия сигнала закончить ввод, в этом случае возвращается
# сигнал закончить ввод
def get_next():
    value = input()
    loop_flag = True
    del_flag = False
    if value == "stop":
        loop_flag = False
        del_flag = True
    else:
        try:
            value = float(value)
        except ValueError:
            print("Введите корректное значение! (Число или stop)")
            del_flag = True

    return value, loop_flag, del_flag


# Умножение всех элементов списка на заданную величину
def multiply():
    index = 0
    for i in task_list:
        task_list[index] = i * DEFAULT_TASK_CONSTANT
        index += 1


# Запись результата выполнения программы в файл
def write_to_file():
    with open(DEFAULT_OUTPUT_FILE, "w") as file:
        for i in task_list:
            file.write(str(i) + "\n")


# Форматированный вывод списка на экран
# Может принимать в качестве параметра строку:
# - Формат вывода
def print_list(value_format="{0:.2f}"):
    for i in task_list:
        print(value_format.format(i))


# Эта процедура может содержать любую
# реализацию сортировки списка
def sort(is_dec):
    task_list.sort(reverse=is_dec)


# Основная процедура, выполняющая программу
def main_loop():
    counter = 0
    print("Чтобы завершить введите stop")
    print("Элемент списка " + counter.__str__())
    value, loop_flag, del_flag = get_next()
    while loop_flag:
        if not del_flag:
            counter += 1
            task_list.append(value)
            print("Элемент списка " + counter.__str__())
        value, loop_flag, del_flag = get_next()
    multiply()
    sort(DEFAULT_IS_DECREMENT_ORDER)
    print_list()
    write_to_file()


# Заход в программу
main_loop()
