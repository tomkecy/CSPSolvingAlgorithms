import numpy as np
import n_queens_solver as nqs


class AppCli:
    INPUT_RUN = 1
    INPUT_CHANGE_CONFIG = 2
    INPUT_EXIT = 3

    LATIN_SQUARE = 'Latin square'
    N_QUEENS = 'N-Queens'

    def __init__(self):
        self._algorithm = nqs.AlgorithmType.backtracking
        self._problem = self.N_QUEENS
        self._n = 1

    def run(self):
        self._print_current_config()
        print('1. Run\n2. Change configuration\n3. Exit')
        input_value = self._get_user_input()

        while input_value != self.INPUT_EXIT:
            if input_value == self.INPUT_RUN:
                self._run_algorithm()
            elif input_value == self.INPUT_CHANGE_CONFIG:
                self._change_config()
            else:
                print('Incorrect input')

            self._print_current_config()
            print('1. Run\n2. Change configuration\n3. Exit')
            input_value = self._get_user_input()

    def _get_user_input(self):
        user_input = None
        while user_input is None:
            try:
                user_input = int(input())
            except ValueError:
                print('Incorrect input, try again')
        return user_input

    def _print_current_config(self):
        print('Problem: %s\nAlgorithm: %s\nN: %s\n' % (self._problem, self._algorithm.value, self._n))

    def _run_algorithm(self):
        alg = nqs.NQueensSolver(self._n)
        res = alg.find_all_solutions()

        if res is not None:
            for solution in res:
                result_matrix = np.zeros(shape=(self._n, self._n))
                for i, j, in solution:
                    result_matrix[i, j] = 1
                print(result_matrix)
            print('Num of solutions for n = %s: %s\n' % (self._n, len(res)))
        else:
            print('No solutions for n=%s\n' % self._n)

    def _change_config(self):
        print('--------------\nChange configuration\n--------------\nCurrent config')
        self._print_current_config()
        print('1. Set problem\n2. Set algorithm\n3. Set n\n4. Return')
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

            print('--------------\nChange configuration\n--------------\nCurrent config')
            self._print_current_config()
            print('1. Set problem\n2. Set algorithm\n3. Set n\n4. Return')
            input_value = self._get_user_input()

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
        self._n = int(input('Enter n: '))
