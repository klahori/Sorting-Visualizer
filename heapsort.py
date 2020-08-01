# Heap Sort
def heap_sort(arr):
    n = len(arr)
    
    # Build a max-heap, Note: You only have to check half of the array and traversing backwards
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, i, n)
    
   
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
       
    return arr

# i: index of element
# n: size of heap
def heapify(arr, i, n):
    # left child
    l = 2 * i + 1
    # right child
    r = 2 * i + 2

    largest = i
    # check left child
    if l < n and arr[l] > arr[i]:
        largest = l
    
    # check right child
    if r < n and arr[largest] < arr[r]:
        largest = r

    # swap if any of the childs need to changed
    if largest != i:
        arr[largest], arr[i] =  arr[i], arr[largest]
        heapify(arr, largest, n)
    




