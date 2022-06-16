#https://programming-review.com/python/algorithms#binarygap
#https://app.codility.com/c/run/trainingN77GD5-XGS/

'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].


'''


def solution(n):
    '''
    this one is a little tricky to come up w but easy to interpret
    :param n:
    :return:
    '''
    b = bin(n)[2:]   #binary numbers formatted like 0b.....
    s1 = False
    tz = 0  # temp zeros
    mz = 0  # max zeros
    for e in b:
        if e == '1': #start the count or end the count
            mz = max(tz, mz) #!!! this is the tricky part, it needs to come here, b/c you are ending the count, but want to check the count before zeroing out tz
            tz = 0 #if you are on a 1, then ofc the temp 0 count is zero
            s1 = True #and ofc you have hit a 1
        else: #you are on a zero
            if (s1 == True):  #if you have already hit a 1 at all
                tz += 1 #then increment the zero, otherwise you are just hitting leading zeros and should do nothing

    return mz

