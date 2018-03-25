import numpy as np
import backtracking_algorithm as bta

alg = bta.BacktrackingAlgorithm()

n = 2
#res = alg.find_first_solution(n)
res = alg.find_all_solutions(n)
if res is not None:
    for solution in res:
        result_matrix = np.zeros(shape=(n, n))
        for i, j, in solution:
            result_matrix[i, j] = 1
        print(result_matrix)
    print('Num of solutions for n = %s: %s' % (n, len(res)))
else:
    print('No solutions for n=%s' % n)

