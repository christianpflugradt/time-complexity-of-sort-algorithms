def comb_sort(arr):
    g = len(arr)
    swapped = True
    while g != 1 or swapped:
        swapped = False
        g = max(1, (g * 10) // 13)
        for i in range(len(arr) - g):
            if arr[i] > arr[i+g]:
                arr[i], arr[i+g] = arr[i+g], arr[i]
                swapped = True

