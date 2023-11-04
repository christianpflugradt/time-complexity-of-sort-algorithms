from insertion_sort import *
from threading import Thread

thread_count = 8

def bucket_sort(arr):
    maximum = max(arr) + 1
    buckets = [[]] * thread_count
    for i in arr:
        bucket = int(i / (maximum / thread_count))
        buckets[bucket].append(i)
    threads = []
    for i in range(thread_count):
        t = Thread(target=insertion_sort, args=(buckets[i],))
        threads.append(t)
        # insertion_sort(buckets[i])
        t.start()
    for t in threads:
        t.join()
    return [item for bucket in buckets for item in bucket]
