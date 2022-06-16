import unittest, math

import tutorials as t

class TestAlgos(unittest.TestCase):


    def test_ITERATIONS_binary_gap(self):

        for N in range(0, 2000):
            expected = len(max(format(N, 'b').strip('0').split('1'))) #this gets expected value https://stackoverflow.com/questions/48951591/python-find-longest-binary-gap-in-binary-representation-of-an-integer-number
            self.assertEqual(t.ITERATIONS_binary_gap.solution(N), expected)



    def test_ARRAYS(self):

        self.assertEqual(t.ARRAYS_cyclic_rotation.solution([1, 2, 3, 4], 4), [1, 2, 3, 4])
        self.assertEqual(t.ARRAYS_cyclic_rotation.solution([0, 0, 0], 1), [0, 0, 0])
        self.assertEqual(t.ARRAYS_cyclic_rotation.solution([5, 6, 7], 1), [7, 5, 6])

    def test_COUNTING(self):
        #COUNTING_frog_river
        A={}
        A[0] = 1
        A[1] = 3
        A[2] = 1
        A[3] = 4
        A[4] = 2
        A[5] = 3
        A[6] = 5
        A[7] = 4
        self.assertEqual(t.COUNTING_frog_river.solution(5, A), 6)

        NPERM, PERM = {}, {}
        NPERM[0] = 4
        NPERM[1] = 1
        NPERM[2] = 3
        PERM = NPERM.copy() #shallow copy

        PERM[3] = 2

        #COUNTING_permutation_check
        self.assertEqual(t.COUNTING_permutation_check.solution(PERM), 1)
        self.assertEqual(t.COUNTING_permutation_check.solution(NPERM), 0)

if __name__ == '__main__':
    unittest.main()