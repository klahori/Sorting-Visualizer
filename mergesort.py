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