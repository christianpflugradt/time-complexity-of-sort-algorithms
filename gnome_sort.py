def gnome_sort(arr):
    p = 0
    while p < len(arr):
        if p == 0 or arr[p] >= arr[p-1]:
            p += 1
        else:
            arr[p], arr[p-1] = arr[p-1], arr[p]
            p -= 1

