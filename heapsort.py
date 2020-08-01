from random import randrange
# Generate random array
arr = []
size = 10
lower_bound = -15
upper_bound = 15
for i in range(size):
     arr.append(randrange(lower_bound, upper_bound + 1))

def heap_sort(arr):
    return arr
print("Orignial:", arr)
print("Sorted:", arr)