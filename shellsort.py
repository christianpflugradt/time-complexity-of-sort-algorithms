def shellsort(arr):
    g = len(arr)//2
    while g > 0:
        for i in range(g, len(arr)):
            t = arr[i]
            j = i
            while j >= g and arr[j-g] > t:
                arr[j] = arr[j-g]
                j -= g
            arr[j] = t
        g //= 2

