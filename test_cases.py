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

        self.assertEqual(t.COUNTING_countdiv.solution(1,14,2), 7) #1 2x 3 4x 5 6x 7 8x 9 10x 11 12x 13 14x  --> 7 are div by 2, including 14
        self.assertEqual(t.COUNTING_countdiv.my_dumb_solution(1, 14, 2), 7)

    def test_PREFIX_SUMS(self):
        A = {}
        A[0] = 0
        A[1] = 1
        A[2] = 0
        A[3] = 1
        A[4] = 1


        self.assertEqual(t.PREFIX_SUMS_passing_cars.solution(A), 5)#(0, 1), (0, 3), (0, 4), (2, 3), (2, 4)

    def test_STACKS_QUEUES(self):
        '''
        STACKS - FILO, like a stack of pancakes, the First in will be the Last eaten, one that is recently pushed (stacked on top)
        will be the first one popped (eaten)

        QUEUES - FIFO, like a queue for a sausage roll at Gregg's - the first in line (push) will be the first one to get their roll (pop)
        '''

if __name__ == '__main__':
    unittest.main()