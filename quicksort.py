def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        p = arr[0]
        l = [i for i in arr[1:] if i < p]
        r = [i for i in arr[1:] if i >= p]
        return quicksort(l) + [p] + quicksort(r)
