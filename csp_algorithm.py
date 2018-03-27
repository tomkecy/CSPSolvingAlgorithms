class CspAlgorithm:
    def __init__(self, domain, constraints):
        self._found_solutions = []
        self._domain = domain
        self._returns_counter = 0
        self._constraints = constraints

    def find_first_solution(self, n):
        values_list = [None] * n

        res = self._assign_next_value(values_list, self._domain, 0, False)
        return values_list if res else None

    def find_all_solutions(self, n):
        self._found_solutions.clear()
        values_list = [None] * n
        self._assign_next_value(values_list, self._domain, 0, True)
        return self._found_solutions

    def find_all_solutions_fc(self, n):
        self._found_solutions.clear()
        values_list = [None] * n
        self._assign_next_fc(values_list, list(self._domain), 0, True)
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

    def check_constraints_fc(self, to_assign, to_check):
        return self.n_queens_constraint(to_assign, to_check)

    def n_queens_constraint(self, to_assign, to_check):
        m, n = to_assign
        i, j = to_check
        if i == m or j == n:
            return False
        x1 = i - m
        x2 = j - n
        if abs(x1) == abs(x2) and i == (m + x1) and j == (n + x2):
            return False
        return True

    def _assign_next_fc(self, values_list, domain, level, find_all):
        for to_assign in domain:
            values_list[level] = to_assign
            domain_copy = [to_check for to_check in domain if self.check_constraints_fc(to_assign, to_check)]
            if domain_copy:
                self._assign_next_fc(values_list, domain_copy, level+1, find_all)

        if len(values_list) == level + 1:
            solution = list(values_list)
            if not self._is_existing_solution(solution):
                self._found_solutions.append(solution)
                return True
        return False

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
                return self._assign_next_value(values_list, list(domain_iter), level, find_all)
            if find_all:
                return self._assign_next_value(values_list, list(domain_iter), level, find_all)
            return True

        if not self._assign_next_value(values_list, self._domain, level + 1, find_all):
            self._returns_counter += 1
            return self._assign_next_value(values_list, list(domain_iter), level, find_all)

        return False

    def _is_existing_solution(self, solution):
        return any([set(found_solution) == set(solution) for found_solution in
                    self._found_solutions])
