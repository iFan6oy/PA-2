import csv
import math
import random
import timeit

# Python program for implementation of MergeSort
# Merges two subarrays of array_i[].
# First subarray is array_i[l..m]
# Second subarray is array_i[m+1..r]

def merge(array_i, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # Temporary arrays are created
    L = [0] * (n1)
    R = [0] * (n2)

    #Data is copied into temporary arrays L[] and R[]
    for i in range(0, n1):
        L[i] = array_i[l + i]

    for j in range (0, n2):
        R[j] = array_i[m + 1 + j]

    # Temp arrays are merged back into array_i[l...r]
    i = 0 # First index of the first subarray
    j = 0 # First index of the second subarray
    k = l # First index of the merged subarray

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            array_i[k] = L[i]
            i += 1
        else:
            array_i[k] = R[j]
            j += 1

        k += 1

     # Copies the leftover elements of L[] if any are remaining
    while i < n1:
         array_i[k] = L[i]
         i += 1
         k += 1

     # Copies the leftover elements of R[] if any are remaining
    while j < n2:
         array_i[k] = R[j]
         j +=1
         k +=1

# l is for the left index and r is for the right index of the subarray of the array to be sorted
def mergeSort(array_i, l, r):
    if l < r:

        # Same as (l + r)/2 but it avoids overflow for large values for l and h
        m = int((l + (r - 1))/2)

        # Sort first and second halves
        mergeSort(array_i, l, m)
        mergeSort(array_i, m + 1, r)
        merge(array_i, l, m, r)

def main():
    size = 0
    lists = [0] * 10

    ch = 'y'

    # Our header for the .csv file
    header = ['Input n size for Array_i', 'Value of n*log(n)', 'Time spent (in seconds)', 'Value of (n * log(n))/time']

    # Opens our .csv file for data input
    with open('Mergesort_Time.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

                    
        # Writes the header
        writer.writerow(header)
        while ch == 'y' or ch == 'Y':
            n = int(input("Enter a number from 1 to 9 : "))
            if n < 0 or n > 10:
                print("Invalid input, please try again!")
            else:
                for i in range(9):
                    array_i = []
                    for j in range(size):
                        array_i.append(random.randint(0, 300))

                    # Sets array size to 1000 * input value 'n'
                    size = 1000 * n
                    lists[i] = array_i
                    array_i = lists[i]

                v = len(array_i) 
                print("The array is")
                for i in range(v):
                    print (array_i[i], end = " ")

                # Yields our execution time for the program
                # Default timer is used to avoid float division by 0 errors
                start_time = timeit.default_timer()
                mergeSort(array_i, 0, v - 1)
                total_time = timeit.default_timer() - start_time

                print("\n\nSorted array is")
                for i in range(v):
                    print(array_i[i], end = " ")

                print("\n\nTime taken = " + str(total_time) + " seconds")

                # Holds our data values for Input value 'n', n*log(n), execution time, and (n*log(n))/execution time
                data = [n, n*(math.log10(n)), total_time, (n*(math.log(n)))/(total_time)]
                   
                # Writes our data to the .csv file
                writer.writerow(data)

                
                ch = input("\n\nDo you wish to continue? (y/n) : ")[0]

if __name__ == "__main__":
   main()
