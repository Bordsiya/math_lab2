from Methods.NewtonMethod import solve_equation_system_newton
from Utils.GraphMethods import draw_graph_equation_system
from Utils.IOMethods import read_problem_equation_system, print_results


def solve_equation_system():
    print('Решение')

    equation_system = read_problem_equation_system()
    #print(equation_system)

    answer = solve_equation_system_newton(equation_system)
    #print(answer)

    print_results(answer)
    draw_graph_equation_system(equation_system)
