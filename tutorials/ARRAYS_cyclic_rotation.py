#https://app.codility.com/c/run/trainingBPBNCK-BP9/
#https://programming-review.com/python/algorithms#cyclicrotation
#https://stackoverflow.com/questions/54843674/cyclic-rotation-in-python



'''
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index,
and the last element of the array is moved to the first place.
For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
(elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

class Solution { public int[] solution(int[] A, int K); }

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


'''
def solution(A, K):
    #https://stackoverflow.com/questions/54843674/cyclic-rotation-in-python

    old = A
    new = [0] * len(A)
    for i in range(K):
        new[0] = old[-1]  #updates first position of new w last of old, [0,0,0,0] --> [4,0,0,0]  or [4,1,2,3] --> [3,1,2,3]
        new[1:] = old[:-1] #updates rest of new w rest of old [4,0,0,0] --> [4,1,2,3] #shift complete
        old = new.copy()  # new = [4,1,2,3] --> old (which was 1,2,3,4). WITHOUT .copy(), new and old will point to same obj in memory and subs
        #sequent updates (above two lines) will update new and old, not just new with old
    return new


def solution2(a,k):
    #https://programming-review.com/python/algorithms#cyclicrotation
    n=len(a)
    if(n==0):
        return []
    k=k%n #i would nvr come up w that
    a=a[n-k:]+a[0:n-k]
    return a