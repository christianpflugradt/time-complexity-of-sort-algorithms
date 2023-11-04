def strand_sort(arr):
    def strand(arr):
        e, s = 0, [arr.pop(0)]
        while e < len(arr):
            if arr[e] > s[-1]:
                s.append(arr.pop(e))
            else:
                e += 1
        return s
    def merge(arr1, arr2):
        o = []
        while len(arr1) > 0 and len(arr2) > 0:
            o.append(arr1.pop(0) if arr1[0] < arr2[0] else arr2.pop(0))
        o += arr1
        o += arr2
        return o
    o = strand(arr)
    while len(arr) > 0:
        o = merge(o, strand(arr))
    return o
