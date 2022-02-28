from Solvers.NotLinearEquationSolver import solve_equation
from Solvers.NotLinearEquationSystemSolver import solve_equation_system
from Utils.Exceptions import exceptions_arr

equations_species_arr = [
    'Нелинейное уравнение',
    'Нелинейная система уравнений'
]


#Выбор вида уравнения
print('Что именно вы хотите решить?')
for i in range(len(equations_species_arr)):
    print(i, ': ', equations_species_arr[i])

inp = input('Выберите нужный номер: ').strip()

try:
    inp = int(inp)
    if 0 <= inp < len(equations_species_arr):
        if inp == 0:
            solve_equation()
        else:
            solve_equation_system()
    else:
        print('Ошибка: ', exceptions_arr['WrongLimitsArgument'])
        exit(1)
except ValueError:
    print('Ошибка: ', exceptions_arr['ValueError'])
    exit(1)
