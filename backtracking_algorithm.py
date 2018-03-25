from itertools import product


class BacktrackingAlgorithm:
    NUM_OF_DIMENSIONS = 2

    def __init__(self):
        pass

    def find_first_solution(self, n):

        domain = list(product(range(0, n), repeat=self.NUM_OF_DIMENSIONS))
        values_list = [None] * n

        res = self._assign_next_value(values_list, domain, 0)

        return values_list if res else None

    def find_all_solutions(self, n):
        domain = list(product(range(0, n), repeat=self.NUM_OF_DIMENSIONS))
        results = []
        values_list = [None] * n
        while self._assign_next_value(values_list, domain, 0) and len(domain) >= n:
            results.append(list(values_list))
            index = domain.index(values_list[0])
            domain = domain[index+1:]
        return results

    def check_constraints(self, values, to_assign):
        m, n = to_assign
        for i, j in values:
            if i == m or j == n:
                return False
            x1 = i - m
            x2 = j - n
            if abs(x1) == abs(x2) and i == (m+x1) and j == (n+x2):
                return False
        return True

    def _assign_next_value(self, values_list, domain, level):
        domain_iter = iter(domain)
        try:
            to_assign = next(domain_iter)
            while not self.check_constraints(values_list[:level], to_assign):
                to_assign = next(domain_iter)
        except StopIteration:
            return False
        values_list[level] = to_assign
        if len(values_list) == level+1:
            return True
        if not self._assign_next_value(values_list, domain, level+1):
            values_list[level] = None
            return self._assign_next_value(values_list, list(domain_iter), level)
        return None not in values_list


