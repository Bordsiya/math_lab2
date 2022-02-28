from Model.Answer import Answer
from Model.EquationSystem import EquationSystem, get_derivative_by_x, get_derivative_by_y, get_function_result

MAX_operations = 10000
offset = 0.000001


def calculate_jacobian(equation_system: EquationSystem, x0: float, y0: float) -> float:
    return get_derivative_by_x(equation_system.equation_types[0], x0, y0) \
           * get_derivative_by_y(equation_system.equation_types[1], x0, y0) \
           - get_derivative_by_y(equation_system.equation_types[0], x0, y0) \
           * get_derivative_by_x(equation_system.equation_types[1], x0, y0)


def get_delta_x(equation_system: EquationSystem, x0: float, y0: float) -> float:
    return get_function_result(equation_system.equation_types[0], x0, y0) \
           * get_derivative_by_y(equation_system.equation_types[1], x0, y0) \
           - get_derivative_by_y(equation_system.equation_types[0], x0, y0) \
           * get_function_result(equation_system.equation_types[1], x0, y0)


def get_delta_y(equation_system: EquationSystem, x0: float, y0: float) -> float:
    return get_derivative_by_x(equation_system.equation_types[0], x0, y0) \
           * get_function_result(equation_system.equation_types[1], x0, y0) \
           - get_function_result(equation_system.equation_types[0], x0, y0) \
           * get_derivative_by_x(equation_system.equation_types[1], x0, y0)


def solve_equation_system_newton(equation_system: EquationSystem) -> Answer:
    last_x = equation_system.x0
    last_y = equation_system.y0

    jacobian = calculate_jacobian(equation_system, last_x, last_y)
    if jacobian == 0:
        last_x -= offset
        jacobian = calculate_jacobian(equation_system, last_x, last_y)

    x = last_x - get_delta_x(equation_system, last_x, last_y) / jacobian
    y = last_y - get_delta_y(equation_system, last_x, last_y) / jacobian
    iteration_amount = 1
    #print('/', last_x, last_y, x, y, abs(x - last_x), abs(y - last_y), iteration_amount)

    while abs(x - last_x) > equation_system.accuracy \
            or abs(y - last_y) > equation_system.accuracy:
        last_x = x
        last_y = y

        jacobian = calculate_jacobian(equation_system, last_x, last_y)
        if jacobian == 0:
            last_x -= offset
            jacobian = calculate_jacobian(equation_system, last_x, last_y)
        x = last_x - get_delta_x(equation_system, last_x, last_y) / jacobian
        y = last_y - get_delta_y(equation_system, last_x, last_y) / jacobian

        #print('/', last_x, last_y, x, y, abs(x - last_x), abs(y - last_y), iteration_amount)

        iteration_amount += 1
        if iteration_amount > MAX_operations:
            return Answer(0, 0, 0, False, 'Не нашлось решение за максимальное количество операций')

    return Answer(x, y, iteration_amount, True, '')
