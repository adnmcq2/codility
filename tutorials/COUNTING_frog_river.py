'''

counting FrogRiverOne

A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.
You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.
The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.
For example, you are given integer X = 5 and array A such that:
A[0] = 1 A[1] = 3 A[2] = 1 A[3] = 4 A[4] = 2 A[5] = 3 A[6] = 5 A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.
Write a function:
def solution(X, A)
that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.
If the frog is never able to jump to the other side of the river, the function should return −1.
For example, given X = 5 and array A such that:
A[0] = 1 A[1] = 3 A[2] = 1 A[3] = 4 A[4] = 2 A[5] = 3 A[6] = 5 A[7] = 4
the function should return 6, as explained above.
'''

def solution(X, A):
    '''


    :param X: length of the river, need to get to X+1
    :param A: is the dict like A[0] = 1 A[1] = 3 A[2] = 1 A[3] = 4 A[4] = 2 A[5] = 3 A[6] = 5 A[7] = 4
    where the key is a time in seconds and the val is a position that leaf fell
    :return:
    '''

    positions = set() #initialize this, which we will need later

    for second in range(len(A)): #
        position = A[second]
        if not position in positions: positions.add(position)   #ok, if at that second, a leaf landed on an empty position, add it to positions

        #you want to return the earliest time the frog can jump across the river. That is going to be when X positions are filled
        if len(positions)==X: return second

    return -1

