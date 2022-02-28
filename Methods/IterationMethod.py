from Model.Answer import Answer
from Model.Equation import Equation, get_derivative_result, get_function_result

MAX_operations = 10000


def get_lambda(equation: Equation) -> float:
    return -1 / max(get_derivative_result(equation.equation_type, equation.a),
                    get_derivative_result(equation.equation_type, equation.b))


def calculate_fi(equation: Equation, last_x: float) -> float:
    return last_x + get_lambda(equation) * get_function_result(equation.equation_type, last_x)


def get_derivative_fi(equation: Equation, x: float) -> float:
    return 1 + get_lambda(equation) * get_derivative_result(equation.equation_type, x)


def check_convergence(equation: Equation, x: float) -> bool:
    return abs(get_derivative_fi(equation, x)) >= 1


def solve_equation_iteration(equation: Equation) -> Answer:
    last_x = equation.a
    x = calculate_fi(equation, last_x)
    iteration_amount = 1

    while abs(x - last_x) > equation.accuracy:
        if check_convergence(equation, x):
            return Answer(0, 0, 0, False, 'Метод расходится')

        #print('/', last_x, x, get_function_result(equation.equation_type, x), abs(x - last_x), iteration_amount)
        last_x = x
        x = calculate_fi(equation, last_x)
        iteration_amount += 1
        if iteration_amount > MAX_operations:
            return Answer(0, 0, 0, False, 'Не нашлось решение за максимальное количество операций')

    #print('/', last_x, x, get_function_result(equation.equation_type, x), abs(x - last_x), iteration_amount)
    return Answer(x, get_function_result(equation.equation_type, x), iteration_amount, True, '')