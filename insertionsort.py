# Insertion Sort
def insertion_sort(arr):
     
     for i in range(len(arr)):
          j = i - 1
          key = arr[i] 
          while j >= 0 and key < arr[j]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j] 
               j -=1
               
     return arr

