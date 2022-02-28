from dataclasses import dataclass


@dataclass
class EquationSystem:
    equation_types: list[int]
    solution_type: int
    x0: int
    y0: int
    accuracy: float


equation_system_type_arr = [
    'x^2 + y^2 - 4 = 0',
    'y - 3x^2 = 0',
    '0.1x^2 + x + 0.2y^2 - 0.3 = 0',
    '0.2x^2 + y - 0.1xy - 0.7 = 0'
]


def get_function_system(eq_type: int):
    if eq_type == 0:
        return lambda x, y: x**2 + y**2 - 4
    elif eq_type == 1:
        return lambda x, y: y - 3 * x**2
    elif eq_type == 2:
        return lambda x, y: 0.1 * x**2 + x + 0.2 * y**2 - 0.3
    elif eq_type == 3:
        return lambda x, y: 0.2 * x**2 + y - 0.1 * x * y - 0.7


def get_function_result(equation_system_type: int, x0: float, y0: float) -> float:
    if equation_system_type == 0:
        return x0**2 + y0**2 - 4
    elif equation_system_type == 1:
        return y0 - 3 * x0**2
    elif equation_system_type == 2:
        return 0.1 * x0**2 + x0 + 0.2 * y0**2 - 0.3
    elif equation_system_type == 3:
        return 0.2 * x0**2 + y0 - 0.1 * x0 * y0 - 0.7


def get_derivative_by_x(equation_system_type: int, x0: float, y0: float) -> float:
    if equation_system_type == 0:
        return 2 * x0
    elif equation_system_type == 1:
        return -3 * 2 * x0
    elif equation_system_type == 2:
        return 0.1 * x0**2 + 1
    elif equation_system_type == 3:
        return 0.2 * 2 * x0 - 0.1 * y0


def get_derivative_by_y(equation_system_type: int, x0: float, y0: float) -> float:
    if equation_system_type == 0:
        return 2 * y0
    elif equation_system_type == 1:
        return 1
    elif equation_system_type == 2:
        return 0.2 * 2 * y0
    elif equation_system_type == 3:
        return 1 - 0.1 * x0
