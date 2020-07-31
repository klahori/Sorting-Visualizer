from random import randrange
# Generate random array in range [-15, 15] with size 30.
arr = []
size = 30
for i in range(size):
     arr.append(randrange(-15,16))
 
print("Orignial:", arr)
# Bubble Sort Non-optomized
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
