from csp_algorithm import *
import numpy as np


class LatinSquareSolver:
    def __init__(self, n):
        self._n = n
        self._domain = [i + 1 for i in range(n)]
        self._variables = [None] * n * n

    def find_all_solutions(self):
        csp_algorithm = CspAlgorithm(self._variables, self._domain, [self._latin_square_constraint], AlgorithmType.backtracking)
        res = csp_algorithm.find_all_solutions(self._n)
        if res:
            print(np.array(res).reshape((self._n, self._n)))
        return res

    def find_all_solutions_fc(self):
        csp_algorithm = CspAlgorithm(self._variables, self._domain, [self._latin_square_constraint], AlgorithmType.forward_checking)
        return csp_algorithm.find_all_solutions(self._n)

    def _latin_square_constraint(self, variable_index, val_to_assign, assigned_variables):
        m, n = variable_index//self._n, variable_index % self._n
        for assigned_var_index in range(len(assigned_variables)):
            i, j = assigned_var_index//self._n, assigned_var_index % self._n

            if val_to_assign == assigned_variables[assigned_var_index] and (m == i or n == j):
                return False
        return True
