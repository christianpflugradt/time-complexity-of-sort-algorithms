def cocktail_sort(arr):
    swapped = True
    s = 0
    e = len(arr) - 1
    while swapped:
        swapped = False
        for i in range(s, e):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        e -= 1
        for i in range(s, e):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        s += 1

