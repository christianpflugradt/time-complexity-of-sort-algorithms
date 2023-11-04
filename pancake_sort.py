def pancake_sort(arr):
    def flip(arr, i):
        s = 0
        while s < i:
            arr[i], arr[s] = arr[s], arr[i]
            s += 1
            i -= 1
    s = len(arr)
    while s > 1:
        m = arr.index(max(arr[:s]))
        if m != s-1:
            flip(arr, m)
            flip(arr, s-1)
        s -= 1

