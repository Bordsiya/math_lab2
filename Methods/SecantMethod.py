from Model.Answer import Answer
from Model.Equation import Equation, get_function_result, get_double_derivative_result

MAX_operations = 10000


def get_initial_approximation(equation: Equation) -> float:
    if (get_function_result(equation.equation_type, equation.a)
            * get_double_derivative_result(equation.equation_type, equation.a) > 0):
        return equation.a
    else:
        return equation.b


def calculate_new_x(equation_type: int, last_last_x: float, last_x: float):
    f_last_x = get_function_result(equation_type, last_x)
    f_last_last_x = get_function_result(equation_type, last_last_x)
    return last_x - ((last_x - last_last_x)
                     * f_last_x) / (f_last_x - f_last_last_x)


def solve_equation_secant(equation: Equation) -> Answer:
    last_last_x = get_initial_approximation(equation)
    last_x = (equation.a + equation.b) / 2
    iteration_amount = 1
    #print('/', last_last_x, last_x, get_function_result(equation.equation_type, last_x), abs(last_x - last_last_x), iteration_amount)

    if abs(last_x - last_last_x) <= equation.accuracy:
        return Answer(last_x, get_function_result(equation.equation_type, last_x), iteration_amount, True, '')

    x = calculate_new_x(equation.equation_type, last_last_x, last_x)
    iteration_amount += 1

    while abs(x - last_x) > equation.accuracy:
        #print('/', last_x, x, get_function_result(equation.equation_type, x), abs(x - last_x), iteration_amount)
        last_last_x = last_x
        last_x = x
        x = calculate_new_x(equation.equation_type, last_last_x, last_x)
        iteration_amount += 1
        if iteration_amount > MAX_operations:
            return Answer(0, 0, 0, False, 'Не нашлось решение за максимальное количество операций')

    #print('/', last_x, x, get_function_result(equation.equation_type, x), abs(x - last_x), iteration_amount)
    return Answer(x, get_function_result(equation.equation_type, x), iteration_amount, True, '')

