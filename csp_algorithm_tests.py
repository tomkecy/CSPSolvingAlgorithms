import unittest
import n_queens_solver as nqs
import latin_square_solver as lss


class CspAlgorithmTests(unittest.TestCase):
    _n_queens_all_solutions = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184]
    _latin_square_all_solutions = [1, 2, 12, 576, 161280]

    def n_queens_find_all_bt_test(self):
        n_upper_limit = 6
        for n in range(1, n_upper_limit):

            bt_alg = nqs.NQueensSolver(n)

            results = bt_alg.find_all_solutions()

            self.assertEqual(len(results), self._n_queens_all_solutions[n - 1],
                             'Incorrect num of solutions for n = %s\n%s != %s' % (
                             n, len(results), self._n_queens_all_solutions[n - 1]))

    @unittest.skip
    def n_queens_find_all_fc_test(self):
        n_upper_limit = 4
        for n in range(1, n_upper_limit):
            bt_alg = nqs.NQueensSolver(n)

            results = bt_alg.find_all_solutions_fc()

            self.assertEqual(len(results), self._n_queens_all_solutions[n - 1],
                             'Incorrect num of solutions for n = %s\n%s != %s' % (
                             n, len(results), self._n_queens_all_solutions[n - 1]))
    #@unittest.skip
    def latin_square_find_all_bt_test(self):
        n_upper_limit = 4
        results = []
        for n in range(1, n_upper_limit):

            bt_alg = lss.LatinSquareSolver(n)

            results.append(len(bt_alg.find_all_solutions()))

        self.assertListEqual(results, self._latin_square_all_solutions[:n_upper_limit])
            #self.assertEqual(len(results), self._latin_square_all_solutions[n - 1],
            #                 'Incorrect num of solutions for n = %s\n%s != %s' % (
            #                 n, len(results), self._latin_square_all_solutions[n - 1]))


if __name__ == '__main__':
    unittest.main()
