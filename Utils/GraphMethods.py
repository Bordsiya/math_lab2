from Model.Equation import Equation, get_function
from Model.EquationSystem import EquationSystem, get_function_system
import matplotlib.pyplot as plt
import numpy as np


def get_linspace_x_equation_system(equation_type: int):
    if equation_type == 0:
        return np.linspace(-3, 3, 300)
    elif equation_type == 1:
        return np.linspace(-3, 3, 300)
    elif equation_type == 2:
        return np.linspace(-11, 1, 300)
    elif equation_type == 3:
        return np.linspace(-6, 4, 300)


def get_linspace_y_equation_system(equation_type: int):
    if equation_type == 0:
        return np.linspace(-3, 3, 300)
    elif equation_type == 1:
        return np.linspace(0, 13, 300)
    elif equation_type == 2:
        return np.linspace(-4, 4, 300)
    elif equation_type == 3:
        return np.linspace(-4, 2, 300)


def draw_graph_equation_system(equation_system: EquationSystem):
    plt.gcf().canvas.set_window_title("График функции")
    plt.grid()
    axes = plt.gca()

    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.spines['left'].set_position('zero')
    axes.spines['bottom'].set_position('zero')
    axes.set_xlabel('x', loc='right')
    axes.set_ylabel('y', loc='top')
    axes.plot(1, 0, marker=">", ms=5, color='k', transform=axes.get_yaxis_transform(), clip_on=False)
    axes.plot(0, 1, marker="^", ms=5, color='k', transform=axes.get_xaxis_transform(), clip_on=False)

    X1 = get_linspace_x_equation_system(equation_system.equation_types[0])
    Y1 = get_linspace_y_equation_system(equation_system.equation_types[0])
    F1 = get_function_system(equation_system.equation_types[0])
    X1_grid, Y1_grid = np.meshgrid(X1, Y1)
    Z1_grid = F1(X1_grid, Y1_grid)

    plt.contour(
        X1_grid, Y1_grid, Z1_grid, [0]
    )

    X2 = get_linspace_x_equation_system(equation_system.equation_types[1])
    Y2 = get_linspace_y_equation_system(equation_system.equation_types[1])
    F2 = get_function_system(equation_system.equation_types[1])
    X2_grid, Y2_grid = np.meshgrid(X2, Y2)
    Z2_grid = F2(X2_grid, Y2_grid)

    plt.contour(
        X2_grid, Y2_grid, Z2_grid, [0]
    )

    plt.savefig('graph')


def get_linspace_equation(equation_type: int):
    if equation_type == 0:
        return np.linspace(-5, 5, 300)
    elif equation_type == 1:
        return np.linspace(-10, 10, 300)
    elif equation_type == 2:
        return np.linspace(-5, 5, 300)
    elif equation_type == 3:
        return np.linspace(-2, 2, 300)


def draw_graph_equation(equation: Equation):
    plt.gcf().canvas.set_window_title("График функции")
    plt.grid()
    axes = plt.gca()

    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.spines['left'].set_position('zero')
    axes.spines['bottom'].set_position('zero')
    axes.set_xlabel('x', loc='right')
    axes.set_ylabel('y', loc='top')
    axes.plot(1, 0, marker=">", ms=5, color='k', transform=axes.get_yaxis_transform(), clip_on=False)
    axes.plot(0, 1, marker="^", ms=5, color='k', transform=axes.get_xaxis_transform(), clip_on=False)

    X = get_linspace_equation(equation.equation_type)
    F = get_function(equation.equation_type)

    plt.xticks(np.arange(min(X), max(X) + 1, 1.0))
    axes.plot(X, F(X))

    plt.savefig('graph')
