from Methods.NewtonMethod import solve_equation_system_newton
from Utils.IOMethods import read_problem_equation_system, print_results


def solve_equation_system():
    equation_system = read_problem_equation_system()

    answer = [solve_equation_system_newton(equation_system)]

    print_results(answer)
