from itertools import product


class BacktrackingAlgorithm:
    NUM_OF_DIMENSIONS = 2

    def __init__(self):
        self._found_solutions = []
        self._domain = []

    def find_first_solution(self, n):

        domain = list(product(range(0, n), repeat=self.NUM_OF_DIMENSIONS))
        values_list = [None] * n

        res = self._assign_next_value(values_list, domain, 0, False)

        return values_list if res else None

    def find_all_solutions(self, n):
        self._found_solutions.clear()
        self._domain = list(product(range(0, n), repeat=self.NUM_OF_DIMENSIONS))
        results = []
        values_list = [None] * n
        domain = self._domain
        while self._assign_next_value(values_list, domain, 0, True) and len(domain) >= n:
            results.append(list(values_list))
            index = domain.index(values_list[0])
            domain = domain[index + 1:]
        return self._found_solutions

    def check_constraints(self, values, to_assign):
        m, n = to_assign
        for i, j in values:
            if i == m or j == n:
                return False
            x1 = i - m
            x2 = j - n
            if abs(x1) == abs(x2) and i == (m + x1) and j == (n + x2):
                return False
        return True

    def _assign_next_value(self, values_list, domain, level, find_all):
        domain_iter = iter(domain)
        try:
            to_assign = next(domain_iter)
            while not self.check_constraints(values_list[:level], to_assign):
                to_assign = next(domain_iter)
        except StopIteration:
            return False
        values_list[level] = to_assign

        if len(values_list) == level + 1:
            solution = list(values_list)
            if not self._is_existing_solution(solution):
                self._found_solutions.append(solution)
            else:
                values_list[level] = None
                return self._assign_next_value(values_list, list(domain_iter), level, find_all)
            if find_all:
                return self._assign_next_value(values_list, list(domain_iter), level, find_all)
            return True

        if not self._assign_next_value(values_list, self._domain, level + 1, find_all):
            values_list[level] = None
            return self._assign_next_value(values_list, list(domain_iter), level, find_all)

        return None not in values_list

    def _is_existing_solution(self, solution):
        return any([set(found_solution) == set(solution) for found_solution in
                    self._found_solutions])
