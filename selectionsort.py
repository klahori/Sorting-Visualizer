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
