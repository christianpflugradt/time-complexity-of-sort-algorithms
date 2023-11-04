from brick_sort import *
from bubble_sort import *
from bucket_sort import *
from cocktail_sort import *
from comb_sort import *
from cycle_sort import *
from exchange_sort import *
from gnome_sort import *
from heap_sort import *
from insertion_sort import *
from merge_sort import *
from pancake_sort import *
from selection_sort import *
from quicksort import *
from shellsort import *
from slowsort import *
from stooge_sort import *
from strand_sort import *
from tree_sort import *

from random import randrange
from time import process_time

# configuration

INITIAL_SIZE = 32
THRESHOLD_IN_SECONDS = 0.1

# algorithms

algorithms = {
    'brick sort': brick_sort,
    'bubble sort': bubble_sort,
    'bucket sort': bucket_sort,
    'cocktail sort': cocktail_sort,
    'comb sort': comb_sort,
    'cycle sort': cycle_sort,
    'exchange sort': exchange_sort,
    'gnome sort': gnome_sort,
    'heap sort': heap_sort,
    'insertion sort': insertion_sort,
    'merge sort': merge_sort,
    'pancake sort': pancake_sort,
    'quicksort': quicksort,
    'selection sort': selection_sort,
    'shellsort': shellsort,
    # 'slowsort': slowsort,
    # 'stooge sort': stooge_sort,
    'strand sort': strand_sort,
    'tree sort': tree_sort,
}

# actual sorting

rnd =  lambda: randrange(1_000_000_000)

def run_timed(algorithm, data, dur):
    size = len(data)
    start = process_time()
    algorithms[algorithm](data)
    end = process_time()
    growth = f', time growth = {"{:.2f}".format((end-start)/dur)}' if dur > 0 else ''
    dur = end-start
    print(f'size = {str(size).rjust(9)}, elapsed time = {"{:.8f}".format(dur)}s{growth}')
    return dur

results = {}

def add_result(size, algorithm, dur):
    global results
    if size not in results:
        results[size] = {}
    results[size][algorithm] = dur

print('\n= TIME COMPLEXITY COMPARISON\n')
print(f'INITIAL_SIZE={INITIAL_SIZE}\nTHRESHOLD_IN_SECONDS={THRESHOLD_IN_SECONDS}')

for algorithm in algorithms.keys():
    size = INITIAL_SIZE
    dur = 0
    print(f'\n== AVERAGE TIME COMPLEXITY OF: {algorithm.upper()}\n')
    while dur < THRESHOLD_IN_SECONDS:
        dur = run_timed(algorithm, [rnd() for i in range(size)], dur)
        add_result(size, algorithm, dur)
        size *= 2

# evaluation

target_size = INITIAL_SIZE
for size in sorted(results.keys(), reverse=True):
    if len(results[size].keys()) == len(algorithms.keys()):
        target_size = size
        break
print(f'\n= TIME COMPLEXITY RANKING (FOR ARRAY SIZE={target_size})\n')
pos = 1
for algorithm in sorted(results[target_size].items(), key=lambda x:x[1]):
    print(f'{"{:02d}".format(pos)}. {algorithm[0].upper().rjust(16)} ({"{:.5f}".format(algorithm[1])} seconds)')
    pos += 1

print('')
