import unittest
import n_queens_solver as nqs
import latin_square_solver as lss
from csp_algorithm import AlgorithmType


class CspAlgorithmTests(unittest.TestCase):
    _n_queens_all_solutions = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184]
    _latin_square_all_solutions = [1, 2, 12, 576, 161280]
    _n_queens_upper_limit = 5

    def n_queens_find_all_bt_test(self):
        for n in range(1, self._n_queens_upper_limit):
            solver = nqs.NQueensSolver(n)

            results = solver.find_all_solutions(AlgorithmType.backtracking)

            self.assertEqual(len(results), self._n_queens_all_solutions[n - 1],
                             'Incorrect num of solutions for n = %s\n%s != %s' % (
                                 n, len(results), self._n_queens_all_solutions[n - 1]))

    def n_queens_find_all_fc_test(self):
        for n in range(1, self._n_queens_upper_limit):
            solver = nqs.NQueensSolver(n)

            results = solver.find_all_solutions(AlgorithmType.forward_checking)

            self.assertEqual(len(results), self._n_queens_all_solutions[n - 1],
                             'Incorrect num of solutions for n = %s\n%s != %s' % (
                                 n, len(results), self._n_queens_all_solutions[n - 1]))

    def latin_square_find_all_bt_test(self):
        n_upper_limit = 5
        results = []
        for n in range(1, n_upper_limit):
            solver = lss.LatinSquareSolver(n)

            results.append(len(solver.find_all_solutions(AlgorithmType.backtracking)))

        self.assertListEqual(results, self._latin_square_all_solutions[:n_upper_limit - 1])

    def latin_square_find_all_fc_test(self):
        n_upper_limit = 5
        results = []
        for n in range(1, n_upper_limit):
            solver = lss.LatinSquareSolver(n)

            results.append(len(solver.find_all_solutions(AlgorithmType.forward_checking)))

        self.assertListEqual(results, self._latin_square_all_solutions[:n_upper_limit - 1])

    def n_queens_find_first_bt_test(self):
        for n in range(1, self._n_queens_upper_limit):
            solver = nqs.NQueensSolver(n)

            results = solver.find_first_solution(AlgorithmType.backtracking)

            self.assertEqual(len(results), 1 if self._n_queens_all_solutions[n - 1] > 0 else 0,
                             'Incorrect num of solutions for n = %s\nFound solutions: %s' % (n, len(results)))

    def n_queens_find_first_fc_test(self):
        for n in range(1, self._n_queens_upper_limit):
            solver = nqs.NQueensSolver(n)

            results = solver.find_first_solution(AlgorithmType.forward_checking)

            self.assertEqual(len(results), 1 if self._n_queens_all_solutions[n - 1] > 0 else 0,
                             'Incorrect num of solutions for n = %s\nFound solutions: %s' % (n, len(results)))

    def latin_square_find_first_bt_test(self):
        n_upper_limit = 4
        for n in range(1, n_upper_limit):
            solver = lss.LatinSquareSolver(n)

            results = solver.find_first_solution(AlgorithmType.backtracking)

            self.assertEqual(len(results), 1 if self._latin_square_all_solutions[n - 1] > 0 else 0,
                             'Incorrect num of solutions for n = %s\nFound solutions: %s' % (n, len(results)))

    def latin_square_find_first_fc_test(self):
        n_upper_limit = 4
        for n in range(1, n_upper_limit):
            solver = lss.LatinSquareSolver(n)

            results = solver.find_first_solution(AlgorithmType.forward_checking)

            self.assertEqual(len(results), 1 if self._latin_square_all_solutions[n - 1] > 0 else 0,
                             'Incorrect num of solutions for n = %s\nFound solutions: %s' % (n, len(results)))


if __name__ == '__main__':
    unittest.main()
