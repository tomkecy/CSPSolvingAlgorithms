from enum import Enum
from timeit import default_timer as timer


class AlgorithmType(Enum):
    backtracking = 'Backtracking'
    forward_checking = 'Forward checking'


class CspAlgorithm:
    def __init__(self, variables, domain, constraints, algorithm=AlgorithmType.backtracking, solution_comparator=None):
        self._found_solutions = []
        self._domain = domain
        self._constraints = constraints
        self._variables = variables
        self._solution_comparator = solution_comparator

        self._returns_counter = 0
        self._execution_time = 0
        self._recursive_calls = 0

        if algorithm == AlgorithmType.backtracking:
            self._algorithm = self._assign_next_bt
        elif algorithm == AlgorithmType.forward_checking:
            self._algorithm = self._assign_next_fc
        else:
            raise Exception('Invalid algorithm')

    def find_first_solution(self):
        start = timer()
        self._algorithm(self._variables, self._domain, 0, False)
        end = timer()
        self._execution_time = end - start
        return self._found_solutions

    def find_all_solutions(self):
        self._found_solutions.clear()

        start = timer()
        self._algorithm(self._variables, self._domain, 0, True)
        end = timer()
        self._execution_time = end - start
        return self._found_solutions

    def get_last_execution_details(self):
        return self._execution_time, self._recursive_calls, self._returns_counter

    def _check_constraints(self, variable_index, val_to_assign, assigned_variables):
        return all([constraint(variable_index, val_to_assign, assigned_variables) for constraint in self._constraints])

    def _assign_next_fc(self, values_list, domain, level, find_all):
        self._recursive_calls += 1
        is_solution_found = False
        for to_assign in domain:
            if not find_all and self._found_solutions:
                return True
            values_list[level] = to_assign
            domain_copy = [to_check for to_check in domain if
                           self._check_constraints(level, to_assign, values_list[:level])]
            if domain_copy:
                if level == len(values_list) - 1:
                    if not self._is_existing_solution(values_list):
                        solution = list(values_list)
                        self._found_solutions.append(solution)
                        is_solution_found = True
                else:
                    is_solution_found = self._assign_next_fc(values_list, domain_copy, level + 1, find_all)
                    if not is_solution_found:
                        self._returns_counter += 1
        return is_solution_found

    def _assign_next_bt(self, values_list, domain, level, find_all):
        self._recursive_calls += 1
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
                return self._assign_next_bt(values_list, list(domain_iter), level, find_all)
            if find_all:
                return self._assign_next_bt(values_list, list(domain_iter), level, find_all)
            return True

        if not self._assign_next_bt(values_list, self._domain, level + 1, find_all):
            self._returns_counter += 1
            return self._assign_next_bt(values_list, list(domain_iter), level, find_all)

        return True

    def _is_existing_solution(self, solution):
        if self._solution_comparator is None:
            return False
        return any([self._solution_comparator(found_solution, solution) for found_solution in
                    self._found_solutions])
