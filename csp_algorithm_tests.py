import unittest
import n_queens_solver as nqs


class CspAlgorithmTests(unittest.TestCase):
    _n_queens_all_solutions = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184]

    def n_queens_find_all_bt_test(self):
        n_upper_limit = 7
        for n in range(1, n_upper_limit):

            bt_alg = nqs.NQueensSolver(n)

            results = bt_alg.find_all_solutions()

            self.assertEqual(len(results), self._n_queens_all_solutions[n - 1],
                             'Incorrect num of solutions for n = %s\n%s != %s' % (
                             n, len(results), self._n_queens_all_solutions[n - 1]))

    def n_queens_find_all_fc_test(self):
        n_upper_limit = 7
        for n in range(1, n_upper_limit):
            bt_alg = nqs.NQueensSolver(n)

            results = bt_alg.find_all_solutions_fc()

            self.assertEqual(len(results), self._n_queens_all_solutions[n - 1],
                             'Incorrect num of solutions for n = %s\n%s != %s' % (
                             n, len(results), self._n_queens_all_solutions[n - 1]))


if __name__ == '__main__':
    unittest.main()
