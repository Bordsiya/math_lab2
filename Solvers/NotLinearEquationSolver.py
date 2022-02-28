from Methods.IterationMethod import solve_equation_iteration
from Methods.SecantMethod import solve_equation_secant
from Utils.GraphMethods import draw_graph_equation
from Utils.IOMethods import read_problem_equation, print_results


def solve_equation():
    print('Решение')
    equation = read_problem_equation()
    #print(equation)

    if equation.solution_type == 0:
        answer = solve_equation_secant(equation)
    else:
        answer = solve_equation_iteration(equation)
    #print(answer)

    print_results(answer)
    draw_graph_equation(equation)

