'''
QUICK SORT

#based on recursion, on every recursion, pick a pivot
#there will be 3 groups, the pivot, the elements less than the pivot and the elements greater than the pivot
# base case, the groups are length 1

choosing first element as pivot
7 6 10 5 9 8 3 4

6 5 3 4, 7, 10 9 8

5 3 4, 6, 7, 9 8, 10
3 4, 5, 6, 7, 8, 9, 10
3, 4, 5, 6, 7, 8, 9, 10

'''

def quick_sort(s):
    if len(s)<=1: return s

    pivot = s[0]
    left = list(filter(lambda x: x<pivot, s))
    right = list(filter(lambda x: x > pivot, s))
    
    center = [e for e in s if e == pivot]
    
    return quick_sort(left)+center+quick_sort(right)

print(quick_sort([7, 6, 10, 5, 9, 8, 3, 4]))







'''
BUBBLE

#video on Bubble sort in python.
#He was showing some website stepik.org
'''

def bubble_sort_single_pass(arr):
    count = 0
    for i, e in enumerate(arr):
        if i==len(arr)-1: break
        if e > arr[i+1]:  #if item to the left is bigger than item to the right, going to need to switch and register a switch
            arr[i], arr[i+1] = arr[i+1], arr[i]
            count+=1
    return arr, count


arr = [5,7,4,3,8,2]


#a single pass will not do all of them, need to make multiple passes - at most the length of array
for run in range(len(arr)-1):
    arr, count = bubble_sort_single_pass(arr)
    print(arr)
    if count==0: break   #stop if


arr = [91, 92, 93, 93, 95, 94]

for run in range(len(arr)-1):
    arr, count = bubble_sort_single_pass(arr)
    print(arr)
    if count==0: break  #maybe if ==1?? nope, zero


'''
MERGE SORT
'''