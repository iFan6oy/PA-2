import random
import time

# Python program for implementation of MergeSort
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # Temporary arrays are created
    L = [0] * (n1)
    R = [0] * (n2)

    #Data is copied into temporary arrays L[] and R[]
    for i in range(0, n1):
        L[i] = array[l + i]

    for j in range (0, n2):
        R[j] = array[m + 1 + j]

    # Temp arrays are merged back into arr[l...r]
    i = 0 # First index of the first subarray
    j = 0 # First index of the second subarray
    k = l # First index of the merged subarray

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1

        k += 1

     # Copies the leftover elements of L[] if any are remaining
    while i < n1:
         array[k] = L[i]
         i += 1
         k += 1

     # Copies the leftover elements of R[] if any are remaining
    while j < n2:
         array[k] = R[j]
         j +=1
         k +=1

# l is for the left index and r is for the right index of the subarray of the array to be sorted
def mergeSort(array, l, r):
    if l < r:

        # Same as (l + r)/2 but it avoids overflow for large values for l and h
        m = int((l + (r - 1))/2)

        # Sort first and second halves
        mergeSort(array, l, m)
        mergeSort(array, m + 1, r)
        merge(array, l, m, r)

def main():
    size = 1000
    lists = [0] * 10

    for i in range(9):
        array = []
        for j in range(size):
            array.append(random.randint(0, 100))

        size += 1000
        lists[i] = array

    ch = 'y'
    while ch == 'y' or ch == 'Y':
        n = int(input("Enter a number from 1 to 9 : "))
        if n < 0 or n > 9:
            print("Invalid input, please try again!")
        else:
            array = lists[i]

            n = len(array)
            print("The array is")
            for i in range(n):
                print (array[i], end = " ")

            start_time = time.time()
            mergeSort(array, 0, n - 1)
            end_time = time.time()

            print("\n\nSorted array is")
            for i in range(n):
                print(array[i], end = " ")

            print("\n\nTime taken = " + str(end_time - start_time) + " seconds")

            ch = input("\n\nDo you wish to continue? (y/n) : ")[0]

if __name__ == "__main__":
   main()