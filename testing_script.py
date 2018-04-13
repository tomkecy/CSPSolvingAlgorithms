import n_queens_solver as nqs
import latin_square_solver as lss
from csp_algorithm import AlgorithmType

n_queens_upper_limit = 9
latin_square_upper_limit = 12


print('Latin square backtracking searching...')
file = open('latin_square_backtracking_first.csv', 'w')
file.write('n, Exec time, Recursive calls, Returns\n')
for n in range(1, latin_square_upper_limit):
    solver = lss.LatinSquareSolver(n)
    solver.find_first_solution(AlgorithmType.backtracking)
    exec_time, calls, returns = solver.get_last_execution_details()
    file.write('%s,%s,%s,%s\n' % (n, exec_time, calls, returns))
file.close()

print('Latin square forward checking - searching...')
file = open('latin_square_forward_checking_first.csv', 'w')
file.write('n, Exec time, Recursive calls, Returns\n')
for n in range(1, latin_square_upper_limit):
    solver = lss.LatinSquareSolver(n)
    solver.find_first_solution(AlgorithmType.forward_checking)
    exec_time, calls, returns = solver.get_last_execution_details()
    file.write('%s,%s,%s,%s\n' % (n, exec_time, calls, returns))
file.close()


def run_tests_find_all():
    file = open('n_queens_backtracking_first.csv', 'w')
    file.write('n, Exec time, Recursive calls, Returns\n')
    for n in range(1, n_queens_upper_limit):
        solver = nqs.NQueensSolver(n)
        solver.find_all_solutions(AlgorithmType.backtracking)
        exec_time, calls, returns = solver.get_last_execution_details()
        file.write('%s,%s,%s,%s\n' % (n, exec_time, calls, returns))
    file.close()
    file = open('n_queens_forward_checking.csv', 'w')
    file.write('n, Exec time, Recursive calls, Returns\n')
    for n in range(1, n_queens_upper_limit):
        solver = nqs.NQueensSolver(n)
        solver.find_all_solutions(AlgorithmType.forward_checking)
        exec_time, calls, returns = solver.get_last_execution_details()
        file.write('%s,%s,%s,%s\n' % (n, exec_time, calls, returns))
    file.close()
    file = open('latin_square_backtracking.csv', 'w')
    file.write('n, Exec time, Recursive calls, Returns\n')
    for n in range(1, latin_square_upper_limit):
        solver = lss.LatinSquareSolver(n)
        solver.find_all_solutions(AlgorithmType.backtracking)
        exec_time, calls, returns = solver.get_last_execution_details()
        file.write('%s,%s,%s,%s\n' % (n, exec_time, calls, returns))
    file.close()
    file = open('latin_square_forward_checking.csv', 'w')
    file.write('n, Exec time, Recursive calls, Returns\n')
    for n in range(1, latin_square_upper_limit):
        solver = lss.LatinSquareSolver(n)
        solver.find_all_solutions(AlgorithmType.forward_checking)
        exec_time, calls, returns = solver.get_last_execution_details()
        file.write('%s,%s,%s,%s\n' % (n, exec_time, calls, returns))
    file.close()


def run_tests_n_queens_find_first():
    print('N-Queens backtracking - searching...')
    file = open('n_queens_backtracking_first.csv', 'w')
    file.write('n, Exec time, Recursive calls, Returns\n')
    for n in range(1, n_queens_upper_limit):
        solver = nqs.NQueensSolver(n)
        solver.find_first_solution(AlgorithmType.backtracking)
        exec_time, calls, returns = solver.get_last_execution_details()
        file.write('%s,%s,%s,%s\n' % (n, exec_time, calls, returns))
    file.close()

    print('N-Queens forward checking - searching...')
    file = open('n_queens_forward_checking_first.csv', 'w')
    file.write('n, Exec time, Recursive calls, Returns\n')
    for n in range(1, n_queens_upper_limit):
        solver = nqs.NQueensSolver(n)
        solver.find_first_solution(AlgorithmType.forward_checking)
        exec_time, calls, returns = solver.get_last_execution_details()
        file.write('%s,%s,%s,%s\n' % (n, exec_time, calls, returns))
    file.close()