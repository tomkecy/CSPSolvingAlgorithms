from enum import Enum


class AlgorithmType(Enum):
    backtracking = 'backtracking'
    forward_checking = 'forward_checking'


class CspAlgorithm:
    def __init__(self, variables, domain, constraints, algorithm=AlgorithmType.backtracking):
        self._found_solutions = []
        self._domain = domain
        self._returns_counter = 0
        self._constraints = constraints
        self._variables = variables

        if algorithm == AlgorithmType.backtracking:
            self._algorithm = self._assign_next_value
        elif algorithm == AlgorithmType.forward_checking:
            self._algorithm = self._assign_next_fc
        else:
            raise Exception('Invalid algorithm')

    def find_first_solution(self, n):
        res = self._algorithm(self._variables, self._domain, 0, False)
        return self._variables if res else None

    def find_all_solutions(self, n):
        self._found_solutions.clear()
        values_list = self._variables

        self._algorithm(values_list, self._domain, 0, True)
        return self._found_solutions

    def _check_constraints(self, variable_index, val_to_assign, assigned_variables):
        return all([constraint(variable_index, val_to_assign, assigned_variables) for constraint in self._constraints])

    def _assign_next_fc(self, values_list, domain, level, find_all):
        for to_assign in domain:
            values_list[level] = to_assign
            domain_copy = [to_check for to_check in domain if self._check_constraints(level, to_assign, values_list[:level])]
            if domain_copy:
                self._assign_next_fc(values_list, domain_copy, level + 1, find_all)

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
            while not self._check_constraints(level, to_assign, values_list[:level]):
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
        # Bug here for LSS
        return any([set(found_solution) == set(solution) for found_solution in
                    self._found_solutions])
