def cycle_sort(arr):
    for c in range(len(arr) - 1):
        i = arr[c]
        p = c
        for j in range(c+1, len(arr)):
            if arr[j] < i:
                p += 1
        if p == c:
            continue
        while i == arr[p]:
            p += 1
        arr[p], i = i, arr[p]
        while p != c:
            p = c
            for j in range(c + 1, len(arr)):
                if arr[j] < i:
                    p += 1
            while i == arr[p]:
                p += 1
            arr[p], i = i, arr[p]

