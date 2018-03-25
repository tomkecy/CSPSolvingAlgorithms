import unittest
import backtracking_algorithm


class MyTestCase(unittest.TestCase):
    _num_of_all_solutions = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184]

    def find_all_solutions_test(self):
        bt_alg = backtracking_algorithm.BacktrackingAlgorithm()

        for n in range(1, len(self._num_of_all_solutions) + 1):
            results = bt_alg.find_all_solutions(n)
            self.assertEqual(len(results), self._num_of_all_solutions[n-1])

if __name__ == '__main__':
    unittest.main()
