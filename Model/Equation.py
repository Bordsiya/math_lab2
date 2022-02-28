from dataclasses import dataclass
import math
import numpy as np

@dataclass
class Equation:
    equation_type: int
    solution_type: int
    a: float
    b: float
    accuracy: float


equation_type_arr = [
    'x^3 - 0.2x^2 + 0.5x + 1.5 = 0',
    'x^2 - 20sin(x) = 0',
    'x^3 + 2.84x^2 - 5.606x - 14.766 = 0',
    'e^3x - 4 = 0'
]


def get_function(eq_type: int):
    if eq_type == 0:
        return lambda x: x**3 - 0.2 * x**2 + 0.5 * x + 1.5
    elif eq_type == 1:
        return lambda x: x**2 - 20 * np.sin(x)
    elif eq_type == 2:
        return lambda x: x**3 + 2.84 * x**2 - 5.606 * x - 14.766
    elif eq_type == 3:
        return lambda x: np.exp(3 * x) - 4


def get_function_result(eq_type: int, x0: float) -> float:
    if eq_type == 0:
        return x0**3 - 0.2 * x0**2 + 0.5 * x0 + 1.5
    elif eq_type == 1:
        return x0**2 - 20 * math.sin(x0)
    elif eq_type == 2:
        return x0**3 + 2.84 * x0**2 - 5.606 * x0 - 14.766
    elif eq_type == 3:
        return math.exp(3 * x0) - 4


def get_derivative_result(eq_type: int, x0: float) -> float:
    if eq_type == 0:
        return 3 * x0**2 - 0.2 * 2 * x0 + 0.5
    elif eq_type == 1:
        return 2 * x0 - 20 * math.cos(x0)
    elif eq_type == 2:
        return 3 * x0**2 + 2.84 * 2 * x0 - 5.606
    elif eq_type == 3:
        return 3 * math.exp(3 * x0)


def get_double_derivative_result(eq_type: int, x0: float) -> float:
    if eq_type == 0:
        return 3 * 2 * x0 - 0.2 * 2
    elif eq_type == 1:
        return 2 + 20 * math.sin(x0)
    elif eq_type == 2:
        return 3 * 2 * x0 + 2.84 * 2
    elif eq_type == 3:
        return 3 * 3 * math.exp(3 * x0)

