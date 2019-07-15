# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # cur_index = i
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr) -1):
            if arr[smallest_index] > arr[j]:
                smallest_index = j    



        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

       #Setting the range for comparison (first round: n, second round: n-1  and so on)
    for i in range(len(arr)-1,0,-1):

      #Comparing within set range
       for j in range(i):

           #Comparing element with its right side neighbor
           if arr[j] > arr[j+1]:

               #swapping
               temp = arr[j]
               arr[j] = arr[j+1]
               arr[j+1] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr