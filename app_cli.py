import numpy as np
import n_queens_solver as nqs


class AppCli:
    INPUT_EXIT = 3
    NUM_OF_DIMENSIONS = 2

    def __init__(self):
        self._algorithm = nqs.AlgorithmType.backtracking
        self._problem = 'N-Queens'

    def run(self):
        self._print_config()
        print('1. Run\n2. Change configuration\n3. Exit')
        input_value = int(input())

        while input_value != self.INPUT_EXIT:
            n = int(input('Enter n: '))
            alg = nqs.NQueensSolver(n)
            res = alg.find_all_solutions()
            if res is not None:
                for solution in res:
                    result_matrix = np.zeros(shape=(n, n))
                    for i, j, in solution:
                        result_matrix[i, j] = 1
                    print(result_matrix)
                print('Num of solutions for n = %s: %s' % (n, len(res)))
            else:
                print('No solutions for n=%s' % n)

            self._print_config()
            print('1. Run\n2. Change configuration\n3. Exit')
            input_value = int(input())

    def _print_config(self):
        print('--------------\nProblem: %s\nAlgorithm: %s\n--------------' % (self._problem, self._algorithm.value))
