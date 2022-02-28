from Methods.IterationMethod import solve_equation_iteration
from Methods.SecantMethod import solve_equation_secant
from Model.Equation import Equation, get_function_result
from Utils.IOMethods import read_problem_equation, print_results

step = 1.0999999999


def are_many_solutions(equation: Equation) -> list:
    list_segments = []
    a = equation.a
    last_result = get_function_result(equation.equation_type, a)
    while a < equation.b:
        a += step
        new_result = get_function_result(equation.equation_type, a)

        if new_result * last_result < 0:
            list_segments.append({'left': a - step, 'right': a + step})
        print(a - step, last_result, a + step, new_result, len(list_segments))
        last_result = new_result

    return list_segments


def solve_equation():
    equation = read_problem_equation()

    solutions = are_many_solutions(equation)

    if len(solutions) != 1:
        print('Имеет место быть несколько решений')
    answers = []
    for i in range(len(solutions)):
        if len(solutions) != 1:
            equation.a = solutions[i]['left']
            equation.b = solutions[i]['right']
        if equation.solution_type == 0:
            answer = solve_equation_secant(equation)
        else:
            answer = solve_equation_iteration(equation)
        answers.append(answer)

    print_results(answers)


