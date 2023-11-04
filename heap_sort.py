def heap_sort(arr):
    def heap(arr, n, i):
        x = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]: x = l
        if r < n and arr[x] < arr[r]: x = r
        if x != i:
            arr[i], arr[x] = arr[x], arr[i]
            heap(arr, n, x)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)

