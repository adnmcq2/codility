
'''
A non-empty array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.
For example, array A such that:
A[0] = 4 A[1] = 1 A[2] = 3 A[3] = 2
is a permutation, but array A such that:
A[0] = 4 A[1] = 1 A[2] = 3
is not a permutation, because value 2 is missing.
The goal is to check whether array A is a permutation.
Write a function:
def solution(A)
that, given an array A, returns 1 if array A is a permutation and 0 if it is not.
For example, given array A such that:
A[0] = 4 A[1] = 1 A[2] = 3 A[3] = 2
the function should return 1.
Given array A such that:
A[0] = 4 A[1] = 1 A[2] = 3
the function should return 0.

'''

def solution(A):
    # values_set, indices_set = set([v for k, v in A.iteritems()]), set([a for a in range(len(A))])
    # for i in A:
    kv = [(k, v) for k, v in A.items()]
    if set(e[0]+1 for e in kv) - set(e[1] for e in kv) == set():
        return 1  #is a permutation
    else: return 0  #is not
