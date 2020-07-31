from random import randrange
# Generate random array
arr = []
size = 5
lower_bound = -15
upper_bound = 15
for i in range(size):
     arr.append(randrange(lower_bound, upper_bound + 1))

arr = [4, -13, -14, -2, 10]
print("Orignial:", arr)

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    current_min_index = 0

    for i in  range(n):
        for j in range(i, n):
            if arr[j] < arr[current_min_index]:
                current_min_index = j
            print(arr)
        arr[i], arr[current_min_index] = arr[current_min_index], arr[i]

    return arr

print("Sorted:  ", selection_sort(arr))