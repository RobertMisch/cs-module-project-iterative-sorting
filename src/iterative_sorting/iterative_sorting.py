# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for search_index in range(cur_index, len(arr)):
            if arr[search_index] < arr[smallest_index]:
                smallest_index = search_index

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index]= arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # need to check if swapped
    swapped= True
    while swapped:
        swapped = False
    #need to iterate through arr
        for index in range(1, len(arr)):
            #swap the higher and lower values
            if arr[index] < arr[index-1]:
                swapped=True
                arr[index], arr[index-1] = arr[index-1], arr[index]


    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def count_sort(arr, maximum=None):
    # Your code here
    #we need to build an array for each number up to our maximum
    if len(arr)==0:
        return arr
    if maximum==None:
        maximum=0
        for number in arr:
            if number > maximum:
                maximum=number
    count_arr=[] 
    sorted_arr=[]
    for i in range(len(arr)):
        sorted_arr.append(0)
    for i in range(maximum+1):
        count_arr.append(0)
    for number in arr:
        if number >=0:
            count_arr[number]+=1
        else:
            # print("Error, negative numbers not allowed in Count Sort")
            return "Error, negative numbers not allowed in Count Sort"
    for index in range(1, len(count_arr)):
        count_arr[index] = count_arr[index] + count_arr[index-1]
    #so we need to look at our original array value
    #we check the count_arr[og value]
    #whatever number is stored in that index, is the correct placement of the og value
    #then we subtract 1 from the count on the count_arr[og value]
    #then we move to the next index in our og array

    for number in arr:
        sorted_arr[count_arr[number]-1] = number
        count_arr[number]-=1

    return sorted_arr
