# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


def bubble_sort(array):
    start = time.time()
    for i in range(len(array)):

        for j in range(len(array)-i-1):

            if array[j] > array[j+1]:

                array[j], array[j+1] = array[j+1], array[j]
    
    end = time.time()
    timeel = end - start
    print(timeel)


def selection_sort(array):
    start = time.time()
    for i in range(len(array)-1):

        #get new minimum
        min_index = i

        for j in range(i+1, len(array)):

            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    end = time.time()
    timeel = end - start
    print(timeel)


def insertion_sort(array):
    start = time.time()
    for i in range(1, len(array)):

        insert_pos = i
        insert_val = array[insert_pos]

        #     is the position    is the item to the left of the 
        #     bigger than 0?      position bigger?
        while insert_pos > 0 and array[insert_pos - 1] > insert_val:
            
            array[insert_pos-1], array[insert_pos] = array[insert_pos], array[insert_pos-1]

            insert_pos -=1

    end = time.time()
    timeel = end - start
    print(timeel)






# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
