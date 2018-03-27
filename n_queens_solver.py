from itertools import product
from csp_algorithm import *


class NQueensSolver:
    def __init__(self, n):
        self._n = n
        self._domain = list(product(range(0, n), repeat=2))
        self._variables = [None] * n

    def find_all_solutions(self):
        csp_algorithm = CspAlgorithm(self._variables, self._domain, [self._n_queens_constraint], AlgorithmType.backtracking)
        return csp_algorithm.find_all_solutions(self._n)

    def find_all_solutions_fc(self):
        csp_algorithm = CspAlgorithm(self._variables, self._domain, [self._n_queens_constraint], AlgorithmType.forward_checking)
        return csp_algorithm.find_all_solutions(self._n)

    def _n_queens_constraint(self, variable_index, val_to_assign, assigned_variables):
        m, n = val_to_assign
        for i, j in assigned_variables:
            if i == m or j == n:
                return False
            x1 = i - m
            x2 = j - n
            if abs(x1) == abs(x2) and i == (m + x1) and j == (n + x2):
                return False
        return True
