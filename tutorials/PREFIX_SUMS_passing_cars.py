#https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

'''
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in xrange(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

================
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:


'''

#https://stackoverflow.com/questions/23774985/codility-passing-car-how-to-approach-this-problem
'''
You need to count number of cars passings. Cars are positioned on the road 
as input says and start driving into either one of directions. 
When car drives, we can easily see that it will drive by cars moving 
in the opposite direction, but only if they were in front of it. Essentially that can be formulated as:

Imagine array 0..N

Take element X (iterate from 0 to Nth element)

If value of element X is 0 then count how many 1 elements it has on the right

If value of element X is 1 then count how many 0 elements it has on left

Repeat for next X

Sum up and divide by 2 (cos it takes 2 cars to pass each other), that's the answer.

In case with 0 1 0 1 1 we have 3+1+2+2+2 = 10. Divide by 2 = 5 passings.

We don't count pair 2-1 because 2nd car is driving to the East and never passes the 1st car that is driving away from it to the West.
'''

def solution(A):

    # n = len(A)
    # P = [0] * (n + 1)  # I think this problem is a prefix sum, b/c you are going to sum all the k's

    total_crossings = 0
    kvs = A.items()
    vs = [kv[1] for kv in kvs]
    for k, v in kvs:
        if v == 0: #moving right
            total_crossings+=len([v for v in vs[k:] if v==1])  #sum up number moving left that are right of this
        elif v == 1: #moving left
            total_crossings+=len([v for v in vs[:k] if v==0])      #sum up number moving right that are left of this

    return int(total_crossings/2)