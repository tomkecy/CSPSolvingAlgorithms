import numpy as np
import backtracking_algorithm as bta
from enum import Enum


class AppCli:
    INPUT_EXIT = 3

    class _AlgorithmType(Enum):
        backtracking = 'backtracking'
        forward_checking = 'forward_checking'

    def __init__(self):
        self._algorithm = self._AlgorithmType.backtracking
        self._problem = 'N-Queens'

    def run(self):
        self._print_config()
        print('1. Run\n2. Change configuration\n3. Exit')
        input_value = int(input())

        while input_value != self.INPUT_EXIT:
            alg = bta.BacktrackingAlgorithm()
            n = int(input('Enter n: '))
            res = alg.find_all_solutions(n)
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
