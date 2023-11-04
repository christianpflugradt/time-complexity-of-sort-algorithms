def brick_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for s in [0, 1]:
            for i in range(s, len(arr)-1, 2):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swapped = True

