import unittest
import csp_algorithm
from itertools import product


class MyTestCase(unittest.TestCase):
    _all_solutions = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184]

    def find_all_solutions_test(self):
        n_upper_limit = 1
        for n in range(1, n_upper_limit):
            bt_alg = csp_algorithm.CspAlgorithm(list(product(range(0, n), repeat=2)))

            results = bt_alg.find_all_solutions(n)

            self.assertEqual(len(results), self._all_solutions[n - 1],
                             'Incorrect num of solutions for n = %s\n%s != %s' % (
                             n, len(results), self._all_solutions[n - 1]))

    def find_all_solutions_fc_test(self):
        n_upper_limit = 6
        for n in range(1, n_upper_limit):
            bt_alg = csp_algorithm.CspAlgorithm(list(product(range(0, n), repeat=2)))

            results = bt_alg.find_all_solutions_fc(n)

            self.assertEqual(len(results), self._all_solutions[n - 1],
                             'Incorrect num of solutions for n = %s\n%s != %s' % (
                             n, len(results), self._all_solutions[n - 1]))


if __name__ == '__main__':
    unittest.main()
