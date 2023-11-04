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

SIZE = 1024
PRINT_DATA = True

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
    'stooge sort': stooge_sort,
    'strand sort': strand_sort,
    'tree sort': tree_sort,
}

# actual sorting

rnd_data = [randrange(SIZE**2) for i in range(SIZE)]

def run_timed(algorithm):
    data = rnd_data.copy()
    start = process_time()
    algorithms[algorithm](data)
    end = process_time()
    return end-start

results = {}

print('\n= PERFORMANCE COMPARISON\n')
print(f'SIZE={SIZE}\nPRINT_DATA={PRINT_DATA}\n')

for algorithm in algorithms.keys():
    print(f'testing {algorithm}...', end='', flush=True)
    results[algorithm] = run_timed(algorithm)
    print(f' done ({"{:.5f}".format(results[algorithm])} seconds)')

# evaluation

if PRINT_DATA:
    print(f'\n= RANDOM DATA USED FOR ALL ALGORITHMS\n')
    print(rnd_data)

print(f'\n= PERFORMANCE RANKING FOR STATIC DATA\n')
pos = 1
for algorithm in sorted(results.items(), key=lambda x:x[1]):
    print(f'{"{:02d}".format(pos)}. {algorithm[0].upper().rjust(16)} ({"{:.5f}".format(algorithm[1])} seconds)')
    pos += 1

print('')
