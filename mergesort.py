from random import randrange
# Generate random array
arr = []
size = 5
lower_bound = -15
upper_bound = 15
for i in range(size):
     arr.append(randrange(lower_bound, upper_bound + 1))

def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        l = arr[:m]
        r = arr[m:]

        merge_sort(l)
        merge_sort(r)
        
    return arr
print("Orignial:", arr)