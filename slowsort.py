def slowsort(arr, i=0, j=-1):
    if j == -1: j = len(arr)-1
    if i >= j: return
    m = (i + j) // 2
    slowsort(arr, i, m)
    slowsort(arr, m+1, j)
    if arr[m] > arr[j]:
        arr[m], arr[j] = arr[j], arr[m]
    slowsort(arr, i, j-1)

