from random import randrange
# Generate random array
arr = []
size = 5
lower_bound = -15
upper_bound = 15
for i in range(size):
     arr.append(randrange(lower_bound, upper_bound + 1))


# Selection Sort
def selection_sort(arr):
    n = len(arr)
    

    for i in  range(n):
        current_min_index = i
        for j in range(i, n):
            if arr[j] < arr[current_min_index]:
                current_min_index = j

        arr[i], arr[current_min_index] = arr[current_min_index], arr[i]

    return arr
