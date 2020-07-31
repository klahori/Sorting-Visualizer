from random import randrange
# Generate random array
arr = []
size = 30
lower_bound = -15
upper_bound = 15
for i in range(size):
     arr.append(randrange(lower_bound, upper_bound + 1))

print("Orignial:", arr)
# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    swapped = False
    
    # Iterate through the whole array
    for i in range(n):
        # Iterate through the start of the array and the second last item sorted

        for j in range(n-i-1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Breaking the loop early if the array is already sorted.
        if swapped:
            swapped = False
        else:
            return arr

    return arr


print("Sorted:  ", bubble_sort(arr))