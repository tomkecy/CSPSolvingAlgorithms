from itertools import product
from csp_algorithm import *


class NQueensSolver:
    def __init__(self, n):
        self._algorithm = None
        self._n = n
        self._domain = list(product(range(0, n), repeat=2))
        self._variables = [None] * n

    def find_first_solution(self, algorithm):
        self._algorithm = CspAlgorithm(self._variables, self._domain, [self._n_queens_constraint], algorithm)
        return self._algorithm.find_first_solution()

    def find_all_solutions(self, algorithm):
        self._algorithm = CspAlgorithm(self._variables, self._domain, [self._n_queens_constraint],
                                       algorithm, self._solution_comparator)
        return self._algorithm.find_all_solutions()

    def get_last_execution_details(self):
        return self._algorithm.get_last_execution_details()

    def _n_queens_constraint(self, variable_index, val_to_assign, assigned_variables):
        m, n = val_to_assign
        for i, j in assigned_variables:
            if i == m or j == n:
                return False
            x1 = i - m
            x2 = j - n
            if abs(x1) == abs(x2):
                return False
        return True

    def _solution_comparator(self, first_solution, second_solution):
        return set(first_solution) == set(second_solution)
