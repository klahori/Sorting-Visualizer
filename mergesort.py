from random import randrange
# Generate random array
arr = []
size = 10
lower_bound = -15
upper_bound = 15
for i in range(size):
     arr.append(randrange(lower_bound, upper_bound + 1))

print("Orignial:", arr)
def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        l = merge_sort(arr[:m])
        r = merge_sort(arr[m:])
        
        arr = []
        while len(l) > 0 and len(r) > 0:
            if l[0] < r[0]:
                arr.append(l.pop(0))
            else:
                arr.append(r.pop(0))
        
        arr += l
        arr += r
        
    return arr
print("Sorted:", merge_sort(arr))