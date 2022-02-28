from Model.Answer import Answer
from Model.Equation import Equation, equation_type_arr
from Model.EquationSystem import EquationSystem, equation_system_type_arr
from Utils.Exceptions import exceptions_arr
from Utils.GraphMethods import draw_graph_equation, draw_graph_equation_system

equation_solution_type_arr = [
    'Метод секущих',
    'Метод простой итерации'
]


#чтение входных данных для уравнения
def read_problem_equation() -> Equation:
    read_line = input

    def close_file():
        return None

    equation = Equation(0, 0, 0, 0, 0)

    #Ввод номера уравнения
    print('Представлены следующие уравнения:')
    for i in range(len(equation_type_arr)):
        print(i, ': ', equation_type_arr[i])

    inp = input('Выберите номер уравнения: ').strip()

    try:
        inp = int(inp)
        if 0 <= inp < len(equation_type_arr):
            equation.equation_type = inp
        else:
            print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

    draw_graph_equation(equation.equation_type)

    # Выбор метода вычислений
    print('Доступные методы вычислений: ')
    for i in range(len(equation_solution_type_arr)):
        print(i, ': ', equation_solution_type_arr[i])

    inp = input('Выберите метод вычислений: ').strip()

    try:
        inp = int(inp)
        if 0 <= inp < len(equation_solution_type_arr):
            equation.solution_type = inp
        else:
            print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

    #Определение источника ввода исходных данных
    inp = input('Вы желаете ввести исходные данные из файла? y/n: ')

    if inp in ['Y', 'y']:
        file_name = input('Введите имя файла: ').strip()
        try:
            file = open(file_name, 'r')
            read_line = lambda x: file.readline()
            close_file = file.close
        except FileNotFoundError or IOError:
            print('Ошибка: ', exceptions_arr['FileNotFound'])
            exit(1)
    elif inp not in ['N', 'n']:
        print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
        exit(1)

    #Ввод границ интервала
    try:
        inp = read_line('Введите начальное приближение к корню (пример: 0 3): ').strip()
        interval = list(inp.split(" "))
        if len(interval) > 2:
            print('Ошибка: ', exceptions_arr['TooMuchLimits'])
            close_file()
            exit(1)
        a = float(interval[0].replace(',', '.'))
        b = float(interval[1].replace(',', '.'))
        if a > b:
            print('Ошибка: ', exceptions_arr['BiggerLeftLimit'])
            close_file()
            exit(1)
        equation.a = a
        equation.b = b
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        close_file()
        exit(1)

    #Ввод погрешности вычисления
    try:
        inp = read_line('Введите погрешность вычисления: ').strip()
        accuracy = float(inp.replace(',', '.'))
        if accuracy < 0:
            print('Ошибка: ', exceptions_arr['NegativeAccuracy'])
            close_file()
            exit(1)
        equation.accuracy = accuracy
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        close_file()
        exit(1)

    close_file()
    return equation


equation_system_solution_type_arr = [
    'Метод Ньютона'
]


# чтение входных данных для системы уравнений
def read_problem_equation_system() -> EquationSystem:
    read_line = input

    def close_file():
        return None

    equation_system = EquationSystem([], 0, 0, 0, 0)

    # Ввод номеров уравнений
    print('Представлены следующие уравнения:')
    for i in range(len(equation_system_type_arr)):
        print(i, ': ', equation_system_type_arr[i])

    counter = 1
    while counter <= 2:
        print('Выберите номер уравнения ', counter, ': ')
        inp = input().strip()
        try:
            inp = int(inp)
            if inp >= len(equation_system_type_arr):
                print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
                exit(1)
            elif counter > 1 and inp == equation_system.equation_types[counter - 2]:
                print('Ошибка: ', exceptions_arr['RepeatingEquationsNumbers'])
                exit(1)
            else:
                equation_system.equation_types.append(inp)
                counter += 1
        except ValueError:
            print('Ошибка: ', exceptions_arr['ValueError'])
            exit(1)

    draw_graph_equation_system(equation_system.equation_types)

    # Выбор метода вычислений
    print('Доступные методы вычислений: ')
    for i in range(len(equation_system_solution_type_arr)):
        print(i, ': ', equation_system_solution_type_arr[i])

    inp = input('Выберите метод вычислений: ').strip()

    try:
        inp = int(inp)
        if 0 <= inp < len(equation_system_solution_type_arr):
            equation_system.solution_type = inp
        else:
            print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
            exit(1)
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        exit(1)

    # Определение источника ввода исходных данных
    inp = input('Вы желаете ввести исходные данные из файла? y/n: ')

    if inp in ['Y', 'y']:
        file_name = input('Введите имя файла: ').strip()
        try:
            file = open(file_name, 'r')
            read_line = lambda x: file.readline()
            close_file = file.close
        except FileNotFoundError or IOError:
            print('Ошибка: ', exceptions_arr['FileNotFound'])
            exit(1)
    elif inp not in ['N', 'n']:
        print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
        exit(1)

    # Ввод начального приближения к корню
    try:
        inp = read_line('Введите начальное приближение к корню (пример: 0 3): ').strip()
        interval = list(inp.split(" "))
        if len(interval) > 2:
            print('Ошибка: ', exceptions_arr['TooMuchLimits'])
            close_file()
            exit(1)
        equation_system.x0 = float(interval[0].replace(',', '.'))
        equation_system.y0 = float(interval[1].replace(',', '.'))
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        close_file()
        exit(1)

    # Ввод погрешности вычисления
    try:
        inp = read_line('Введите погрешность вычисления: ').strip()
        accuracy = float(inp.replace(',', '.'))
        if accuracy < 0:
            print('Ошибка: ', exceptions_arr['NegativeAccuracy'])
            close_file()
            exit(1)
        equation_system.accuracy = accuracy
    except ValueError:
        print('Ошибка: ', exceptions_arr['ValueError'])
        close_file()
        exit(1)

    return equation_system


#Вывод результатов
def print_results(answers: list[Answer]):
    write_line = print

    def close_file():
        return None

    inp = input('Вы желаете вывести ответ в файл? y/n: ')

    if inp in ['Y', 'y']:
        file_name = input('Введите имя файла: ').strip()
        file = open(file_name, 'w')
        write_line = lambda x: file.write(x)
        close_file = file.close

    elif inp not in ['N', 'n']:
        print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
        exit(1)

    for answer in answers:
        if answer.can_converge:
            write_line('Вычисленный корень: (' + str(answer.x) + ';' + str(answer.y) + ')\n')
            write_line('Затраченное количество итераций: ' + str(answer.iteration_amount) + '\n')
        else:
            write_line(answer.error_message + '\n')

    close_file()
