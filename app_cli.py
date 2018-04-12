import numpy as np
import n_queens_solver as nqs
import latin_square_solver as lss
from csp_algorithm import AlgorithmType


class AppCli:
    INPUT_FIND_FIRST = 1
    INPUT_FIND_ALL = 2
    INPUT_LAST_EXEC_DETAILS = 3
    INPUT_CHANGE_CONFIG = 4
    INPUT_EXIT = 5

    LATIN_SQUARE = 'Latin square'
    N_QUEENS = 'N-Queens'

    MENU_OPTIONS_STRING = '1. Find first solution\n2. Find all solutions\n3. Get last execution details\n' \
                          '4. Change configuration\n5. Exit'
    MENU_HEADER_STRING = '--------------\nMenu\n--------------\n'

    CONFIG_HEADER_STRING = '--------------\nChange configuration\n--------------\n'
    CONFIG_OPTIONS_STRING = '1. Set problem\n2. Set algorithm\n3. Set n\n4. Return'

    def __init__(self):
        self._algorithm = AlgorithmType.backtracking
        self._problem = self.N_QUEENS
        self._n = 1
        self._solver = None

    def run(self):
        self._print_menu()
        input_value = self._get_user_input()

        while input_value != self.INPUT_EXIT:
            if input_value == self.INPUT_FIND_FIRST:
                self._run_algorithm(False)
            elif input_value == self.INPUT_FIND_ALL:
                self._run_algorithm(True)
            elif input_value == self.INPUT_LAST_EXEC_DETAILS:
                self._print_last_exec_details()
            elif input_value == self.INPUT_CHANGE_CONFIG:
                self._change_config()
            else:
                print('Incorrect input')

            self._print_menu()
            input_value = self._get_user_input()

    def _print_menu(self):
        print('%s%s%s' % (self.MENU_HEADER_STRING, self._get_current_config_string(), self.MENU_OPTIONS_STRING))

    def _get_user_input(self, prompt=None):
        user_input = None
        while user_input is None:
            try:
                user_input = int(input()) if prompt is None else int(input(prompt))
            except ValueError:
                print('Incorrect input, try again')
        return user_input

    def _get_current_config_string(self):
        return 'Current config\nProblem: %s\nAlgorithm: %s\nN: %s\n' % (self._problem, self._algorithm.value, self._n)

    def _run_algorithm(self, find_all):
        self._solver = nqs.NQueensSolver(self._n) if self._problem == self.N_QUEENS else lss.LatinSquareSolver(self._n)

        res = self._solver.find_all_solutions(self._algorithm) if find_all \
            else self._solver.find_first_solution(self._algorithm)

        self._print_found_solutions(res, find_all)

    def _print_found_solutions(self, res, find_all):
        if res:
            if self._problem == self.N_QUEENS:
                for solution in res:
                    result_matrix = np.zeros(shape=(self._n, self._n))
                    for i, j, in solution:
                        result_matrix[i, j] = 1
                    print(result_matrix)
            else:
                for solution in res:
                    result_matrix = np.reshape(solution, (self._n, self._n))
                    print(result_matrix)

            if find_all:
                print('\nNum of solutions for n = %s: %s\n' % (self._n, len(res)))
        else:
            print('No solutions for n=%s\n' % self._n)

    def _change_config(self):
        self._print_change_config_menu()
        input_value = self._get_user_input()

        while input_value != 4:
            if input_value == 1:
                self._change_config_problem()
            elif input_value == 2:
                self._change_config_algorithm()
            elif input_value == 3:
                self._change_config_n()
            else:
                print('Incorrect input')

            self._print_change_config_menu()
            input_value = self._get_user_input()

    def _print_change_config_menu(self):
        print('%s%s%s' % (self.CONFIG_HEADER_STRING, self._get_current_config_string(), self.CONFIG_OPTIONS_STRING))

    def _change_config_problem(self):
        print('1. N-Queens\n2. Latin square')
        input_value = self._get_user_input()
        if input_value == 1:
            self._problem = self.N_QUEENS
        elif input_value == 2:
            self._problem = self.LATIN_SQUARE
        else:
            print('Incorrect input')

    def _change_config_algorithm(self):
        print('1. Backtracking\n2. Forward checking')
        input_value = self._get_user_input()
        if input_value == 1:
            self._algorithm = nqs.AlgorithmType.backtracking
        elif input_value == 2:
            self._algorithm = nqs.AlgorithmType.forward_checking
        else:
            print('Incorrect input')

    def _change_config_n(self):
        self._n = self._get_user_input('Enter n:')

    def _print_last_exec_details(self):
        if self._solver is None:
            print('No previous run data!')
        else:
            exec_time, calls, returns = self._solver.get_last_execution_details()
            print('Execution time: %ss\nRecursive calls: %s\nReturns: %s' % (exec_time, calls, returns))
