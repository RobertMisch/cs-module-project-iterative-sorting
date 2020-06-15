import math
def linear_search(arr, target):
    # Your code here
    for index, item in enumerate(arr): 
        if item == target:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left_bound=0
    right_bound= len(arr)-1
    position= math.floor(left_bound+right_bound/2)
    searching=True

    while searching:
        if left_bound>right_bound:
            return -1
        elif target < arr[position]:
            right_bound=position
            position= math.floor(left_bound+right_bound/2)
        elif target > arr[position]:
            left_bound=position
            position= math.floor(left_bound+right_bound/2)
        elif target == arr[position]:
            searching = False
            return position

    # return -1  # not found
