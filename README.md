# Time Complexity of Sorting Algorithms

This repository contains various popular [sorting algorithms](https://en.wikipedia.org/wiki/Sorting_algorithm) written in [Python](https://www.python.org/) and some `main` scripts to compare them regarding time complexity and performance.

## Time Complexity Comparison

Execute as: `python main_time_complexity.py`.

This [script](main_time_complexity.py) will create arrays with random numbers and apply sorting algorithms to them. It will start with a `INITIAL_SIZE` and will create an array with twice that size after successfully sorting it. The time taken is measured and once it exceeds the `THRESHOLD_IN_SECONDS` the next algorithm will be applied. You can tune both parameters in the `# configuration` section of the script. You can also remove algorithms from the `algorithms` dictionary or add your own. Per default [slowsort](slowsort.py) and [stooge sort](stooge_sort.py) are disabled as they take significantly longer than the other algorithms.

For each sorting the time growth compared to the previous sorting is printed. As the data size is doubled on every run for one algorithm a time growth of 2 equals linear growth while a time growth of 4 is quadratic. As all data is random this value can be understood as an average that will differ from run to run. Also keep in mind that the actual processing time is measured which is not equal to the mathematical time complexity as it is influenced by a variety of factors such as the Python runtime and operating system.

After all algorithms are tested the maximum data size all algorithms processed is determined and the algorithms are listed from shortest to longest duration for this data size. Keep in mind that each algorithm received different random data so the performance may vary for different runs.

You'll find sample output of this script further below.

## Performance Comparison

Execute as: `python main_same_data.py`

This [script](main_same_data.py) will create an array for the configured `SIZE` with numbers in range `0 <= number < SIZE**2` and test all algorithms against it. [slowsort](slowsort.py) is disabled by default to allow for a bigger default `SIZE` which would result in slowsort running for hours (it really lives up to its name). As with the Time Complexity Comparison script you may change the `SIZE` in the `# configuration` section as well as print out the static data used by setting `PRINT_DATA` to `True`. You may also remove or enable/add any algorithms.

You'll find sample output of this script further below.

## Sample Outputs

### Time Complexity Comparison

This output was generated with `INITIAL_SIZE=32` and `THRESHOLD_IN_SECONDS=1` on a Manjaro Linux with i5-1035G1 CPU and 8GB of RAM.

```
= TIME COMPLEXITY COMPARISON

INITIAL_SIZE=32
THRESHOLD_IN_SECONDS=1

== AVERAGE TIME COMPLEXITY OF: BRICK SORT

size =        32, elapsed time = 0.00003565s
size =        64, elapsed time = 0.00011147s, time growth = 3.13
size =       128, elapsed time = 0.00041568s, time growth = 3.73
size =       256, elapsed time = 0.00157643s, time growth = 3.79
size =       512, elapsed time = 0.00680926s, time growth = 4.32
size =      1024, elapsed time = 0.02751132s, time growth = 4.04
size =      2048, elapsed time = 0.10914676s, time growth = 3.97
size =      4096, elapsed time = 0.43395390s, time growth = 3.98
size =      8192, elapsed time = 1.77592052s, time growth = 4.09

== AVERAGE TIME COMPLEXITY OF: BUBBLE SORT

size =        32, elapsed time = 0.00003669s
size =        64, elapsed time = 0.00013312s, time growth = 3.63
size =       128, elapsed time = 0.00045169s, time growth = 3.39
size =       256, elapsed time = 0.00158314s, time growth = 3.50
size =       512, elapsed time = 0.00646762s, time growth = 4.09
size =      1024, elapsed time = 0.02935399s, time growth = 4.54
size =      2048, elapsed time = 0.11513358s, time growth = 3.92
size =      4096, elapsed time = 0.46555274s, time growth = 4.04
size =      8192, elapsed time = 1.87023629s, time growth = 4.02

== AVERAGE TIME COMPLEXITY OF: BUCKET SORT

size =        32, elapsed time = 0.00175621s
size =        64, elapsed time = 0.00070072s, time growth = 0.40
size =       128, elapsed time = 0.00080597s, time growth = 1.15
size =       256, elapsed time = 0.00137605s, time growth = 1.71
size =       512, elapsed time = 0.00387739s, time growth = 2.82
size =      1024, elapsed time = 0.01578803s, time growth = 4.07
size =      2048, elapsed time = 0.06028160s, time growth = 3.82
size =      4096, elapsed time = 0.24607126s, time growth = 4.08
size =      8192, elapsed time = 0.91462807s, time growth = 3.72
size =     16384, elapsed time = 3.85885705s, time growth = 4.22

== AVERAGE TIME COMPLEXITY OF: COCKTAIL SORT

size =        32, elapsed time = 0.00003468s
size =        64, elapsed time = 0.00009289s, time growth = 2.68
size =       128, elapsed time = 0.00037210s, time growth = 4.01
size =       256, elapsed time = 0.00146533s, time growth = 3.94
size =       512, elapsed time = 0.00618867s, time growth = 4.22
size =      1024, elapsed time = 0.03166645s, time growth = 5.12
size =      2048, elapsed time = 0.11998698s, time growth = 3.79
size =      4096, elapsed time = 0.52693377s, time growth = 4.39
size =      8192, elapsed time = 1.89535649s, time growth = 3.60

== AVERAGE TIME COMPLEXITY OF: COMB SORT

size =        32, elapsed time = 0.00009023s
size =        64, elapsed time = 0.00006794s, time growth = 0.75
size =       128, elapsed time = 0.00014514s, time growth = 2.14
size =       256, elapsed time = 0.00016169s, time growth = 1.11
size =       512, elapsed time = 0.00039125s, time growth = 2.42
size =      1024, elapsed time = 0.00092326s, time growth = 2.36
size =      2048, elapsed time = 0.00228337s, time growth = 2.47
size =      4096, elapsed time = 0.00567467s, time growth = 2.49
size =      8192, elapsed time = 0.01402362s, time growth = 2.47
size =     16384, elapsed time = 0.02988948s, time growth = 2.13
size =     32768, elapsed time = 0.06773882s, time growth = 2.27
size =     65536, elapsed time = 0.15528026s, time growth = 2.29
size =    131072, elapsed time = 0.32329506s, time growth = 2.08
size =    262144, elapsed time = 1.24327887s, time growth = 3.85

== AVERAGE TIME COMPLEXITY OF: CYCLE SORT

size =        32, elapsed time = 0.00004730s
size =        64, elapsed time = 0.00020106s, time growth = 4.25
size =       128, elapsed time = 0.00065172s, time growth = 3.24
size =       256, elapsed time = 0.00211803s, time growth = 3.25
size =       512, elapsed time = 0.01272538s, time growth = 6.01
size =      1024, elapsed time = 0.04249987s, time growth = 3.34
size =      2048, elapsed time = 0.16612405s, time growth = 3.91
size =      4096, elapsed time = 0.74692734s, time growth = 4.50
size =      8192, elapsed time = 2.75721865s, time growth = 3.69

== AVERAGE TIME COMPLEXITY OF: EXCHANGE SORT

size =        32, elapsed time = 0.00006120s
size =        64, elapsed time = 0.00012474s, time growth = 2.04
size =       128, elapsed time = 0.00038026s, time growth = 3.05
size =       256, elapsed time = 0.00140591s, time growth = 3.70
size =       512, elapsed time = 0.00495835s, time growth = 3.53
size =      1024, elapsed time = 0.02159562s, time growth = 4.36
size =      2048, elapsed time = 0.09290361s, time growth = 4.30
size =      4096, elapsed time = 0.35455403s, time growth = 3.82
size =      8192, elapsed time = 1.49044881s, time growth = 4.20

== AVERAGE TIME COMPLEXITY OF: GNOME SORT

size =        32, elapsed time = 0.00006769s
size =        64, elapsed time = 0.00027481s, time growth = 4.06
size =       128, elapsed time = 0.00111653s, time growth = 4.06
size =       256, elapsed time = 0.00388237s, time growth = 3.48
size =       512, elapsed time = 0.02222927s, time growth = 5.73
size =      1024, elapsed time = 0.08588100s, time growth = 3.86
size =      2048, elapsed time = 0.31695063s, time growth = 3.69
size =      4096, elapsed time = 0.65162787s, time growth = 2.06
size =      8192, elapsed time = 2.91863683s, time growth = 4.48

== AVERAGE TIME COMPLEXITY OF: HEAP SORT

size =        32, elapsed time = 0.00003628s
size =        64, elapsed time = 0.00006048s, time growth = 1.67
size =       128, elapsed time = 0.00013471s, time growth = 2.23
size =       256, elapsed time = 0.00030748s, time growth = 2.28
size =       512, elapsed time = 0.00078214s, time growth = 2.54
size =      1024, elapsed time = 0.00150924s, time growth = 1.93
size =      2048, elapsed time = 0.00395461s, time growth = 2.62
size =      4096, elapsed time = 0.00762462s, time growth = 1.93
size =      8192, elapsed time = 0.01769554s, time growth = 2.32
size =     16384, elapsed time = 0.03942594s, time growth = 2.23
size =     32768, elapsed time = 0.08221384s, time growth = 2.09
size =     65536, elapsed time = 0.19662620s, time growth = 2.39
size =    131072, elapsed time = 0.44877547s, time growth = 2.28
size =    262144, elapsed time = 0.86485184s, time growth = 1.93
size =    524288, elapsed time = 2.24158661s, time growth = 2.59

== AVERAGE TIME COMPLEXITY OF: INSERTION SORT

size =        32, elapsed time = 0.00004435s
size =        64, elapsed time = 0.00006807s, time growth = 1.53
size =       128, elapsed time = 0.00018957s, time growth = 2.79
size =       256, elapsed time = 0.00077205s, time growth = 4.07
size =       512, elapsed time = 0.00301668s, time growth = 3.91
size =      1024, elapsed time = 0.01420105s, time growth = 4.71
size =      2048, elapsed time = 0.04997768s, time growth = 3.52
size =      4096, elapsed time = 0.20143446s, time growth = 4.03
size =      8192, elapsed time = 0.79945807s, time growth = 3.97
size =     16384, elapsed time = 3.56010766s, time growth = 4.45

== AVERAGE TIME COMPLEXITY OF: MERGE SORT

size =        32, elapsed time = 0.00008085s
size =        64, elapsed time = 0.00005478s, time growth = 0.68
size =       128, elapsed time = 0.00010581s, time growth = 1.93
size =       256, elapsed time = 0.00037382s, time growth = 3.53
size =       512, elapsed time = 0.00053161s, time growth = 1.42
size =      1024, elapsed time = 0.00156245s, time growth = 2.94
size =      2048, elapsed time = 0.00259523s, time growth = 1.66
size =      4096, elapsed time = 0.00546948s, time growth = 2.11
size =      8192, elapsed time = 0.01358289s, time growth = 2.48
size =     16384, elapsed time = 0.02963762s, time growth = 2.18
size =     32768, elapsed time = 0.05504476s, time growth = 1.86
size =     65536, elapsed time = 0.11535118s, time growth = 2.10
size =    131072, elapsed time = 0.25824095s, time growth = 2.24
size =    262144, elapsed time = 0.59996893s, time growth = 2.32
size =    524288, elapsed time = 1.14315103s, time growth = 1.91

== AVERAGE TIME COMPLEXITY OF: PANCAKE SORT

size =        32, elapsed time = 0.00005501s
size =        64, elapsed time = 0.00016942s, time growth = 3.08
size =       128, elapsed time = 0.00042594s, time growth = 2.51
size =       256, elapsed time = 0.00166722s, time growth = 3.91
size =       512, elapsed time = 0.00684705s, time growth = 4.11
size =      1024, elapsed time = 0.02702536s, time growth = 3.95
size =      2048, elapsed time = 0.10239318s, time growth = 3.79
size =      4096, elapsed time = 0.45092851s, time growth = 4.40
size =      8192, elapsed time = 1.88170696s, time growth = 4.17

== AVERAGE TIME COMPLEXITY OF: QUICKSORT

size =        32, elapsed time = 0.00006422s
size =        64, elapsed time = 0.00018105s, time growth = 2.82
size =       128, elapsed time = 0.00012885s, time growth = 0.71
size =       256, elapsed time = 0.00029867s, time growth = 2.32
size =       512, elapsed time = 0.00045843s, time growth = 1.53
size =      1024, elapsed time = 0.00111819s, time growth = 2.44
size =      2048, elapsed time = 0.00206543s, time growth = 1.85
size =      4096, elapsed time = 0.00456234s, time growth = 2.21
size =      8192, elapsed time = 0.01065073s, time growth = 2.33
size =     16384, elapsed time = 0.02232834s, time growth = 2.10
size =     32768, elapsed time = 0.04504909s, time growth = 2.02
size =     65536, elapsed time = 0.09789956s, time growth = 2.17
size =    131072, elapsed time = 0.20779363s, time growth = 2.12
size =    262144, elapsed time = 0.51009903s, time growth = 2.45
size =    524288, elapsed time = 1.16700189s, time growth = 2.29

== AVERAGE TIME COMPLEXITY OF: SELECTION SORT

size =        32, elapsed time = 0.00005555s
size =        64, elapsed time = 0.00006159s, time growth = 1.11
size =       128, elapsed time = 0.00028379s, time growth = 4.61
size =       256, elapsed time = 0.00088654s, time growth = 3.12
size =       512, elapsed time = 0.00355997s, time growth = 4.02
size =      1024, elapsed time = 0.01633300s, time growth = 4.59
size =      2048, elapsed time = 0.06232368s, time growth = 3.82
size =      4096, elapsed time = 0.23939814s, time growth = 3.84
size =      8192, elapsed time = 0.96385696s, time growth = 4.03
size =     16384, elapsed time = 4.15416630s, time growth = 4.31

== AVERAGE TIME COMPLEXITY OF: SHELLSORT

size =        32, elapsed time = 0.00002311s
size =        64, elapsed time = 0.00002989s, time growth = 1.29
size =       128, elapsed time = 0.00007492s, time growth = 2.51
size =       256, elapsed time = 0.00020168s, time growth = 2.69
size =       512, elapsed time = 0.00055801s, time growth = 2.77
size =      1024, elapsed time = 0.00127194s, time growth = 2.28
size =      2048, elapsed time = 0.00388506s, time growth = 3.05
size =      4096, elapsed time = 0.01263689s, time growth = 3.25
size =      8192, elapsed time = 0.03384066s, time growth = 2.68
size =     16384, elapsed time = 0.07339683s, time growth = 2.17
size =     32768, elapsed time = 0.23488721s, time growth = 3.20
size =     65536, elapsed time = 0.67221294s, time growth = 2.86
size =    131072, elapsed time = 1.52912343s, time growth = 2.27

== AVERAGE TIME COMPLEXITY OF: STRAND SORT

size =        32, elapsed time = 0.00004260s
size =        64, elapsed time = 0.00005677s, time growth = 1.33
size =       128, elapsed time = 0.00016881s, time growth = 2.97
size =       256, elapsed time = 0.00035992s, time growth = 2.13
size =       512, elapsed time = 0.00110830s, time growth = 3.08
size =      1024, elapsed time = 0.00305885s, time growth = 2.76
size =      2048, elapsed time = 0.01154161s, time growth = 3.77
size =      4096, elapsed time = 0.04252700s, time growth = 3.68
size =      8192, elapsed time = 0.19561090s, time growth = 4.60
size =     16384, elapsed time = 1.15270718s, time growth = 5.89

== AVERAGE TIME COMPLEXITY OF: TREE SORT

size =        32, elapsed time = 0.00004874s
size =        64, elapsed time = 0.00003360s, time growth = 0.69
size =       128, elapsed time = 0.00008861s, time growth = 2.64
size =       256, elapsed time = 0.00015055s, time growth = 1.70
size =       512, elapsed time = 0.00037979s, time growth = 2.52
size =      1024, elapsed time = 0.00088685s, time growth = 2.34
size =      2048, elapsed time = 0.00186359s, time growth = 2.10
size =      4096, elapsed time = 0.00482966s, time growth = 2.59
size =      8192, elapsed time = 0.01081561s, time growth = 2.24
size =     16384, elapsed time = 0.02745410s, time growth = 2.54
size =     32768, elapsed time = 0.06695237s, time growth = 2.44
size =     65536, elapsed time = 0.14971834s, time growth = 2.24
size =    131072, elapsed time = 0.26835411s, time growth = 1.79
size =    262144, elapsed time = 0.75241471s, time growth = 2.80
size =    524288, elapsed time = 2.11942123s, time growth = 2.82

= TIME COMPLEXITY RANKING (FOR ARRAY SIZE=8192)

01.        QUICKSORT (0.01065 seconds)
02.        TREE SORT (0.01082 seconds)
03.       MERGE SORT (0.01358 seconds)
04.        COMB SORT (0.01402 seconds)
05.        HEAP SORT (0.01770 seconds)
06.        SHELLSORT (0.03384 seconds)
07.      STRAND SORT (0.19561 seconds)
08.   INSERTION SORT (0.79946 seconds)
09.      BUCKET SORT (0.91463 seconds)
10.   SELECTION SORT (0.96386 seconds)
11.    EXCHANGE SORT (1.49045 seconds)
12.       BRICK SORT (1.77592 seconds)
13.      BUBBLE SORT (1.87024 seconds)
14.     PANCAKE SORT (1.88171 seconds)
15.    COCKTAIL SORT (1.89536 seconds)
16.       CYCLE SORT (2.75722 seconds)
17.       GNOME SORT (2.91864 seconds)
```
### Performance Comparison with Big Array

This output was generated with `SIZE=65536` and `PRINT_DATA=False` on Manjaro Linux with i5-1035G1 CPU.

```
= PERFORMANCE COMPARISON

SIZE=65536
PRINT_DATA=False

testing brick sort... done (161.36594 seconds)
testing bubble sort... done (138.07153 seconds)
testing bucket sort... done (65.85098 seconds)
testing cocktail sort... done (123.18565 seconds)
testing comb sort... done (0.18011 seconds)
testing cycle sort... done (227.94288 seconds)
testing exchange sort... done (102.28614 seconds)
testing gnome sort... done (329.78730 seconds)
testing heap sort... done (0.19156 seconds)
testing insertion sort... done (59.93059 seconds)
testing merge sort... done (0.12096 seconds)
testing pancake sort... done (138.13012 seconds)
testing quicksort... done (0.11600 seconds)
testing selection sort... done (104.74053 seconds)
testing shellsort... done (0.57068 seconds)
testing strand sort... done (33.83931 seconds)
testing tree sort... done (0.14907 seconds)

= PERFORMANCE RANKING FOR STATIC DATA

01.        QUICKSORT (0.11600 seconds)
02.       MERGE SORT (0.12096 seconds)
03.        TREE SORT (0.14907 seconds)
04.        COMB SORT (0.18011 seconds)
05.        HEAP SORT (0.19156 seconds)
06.        SHELLSORT (0.57068 seconds)
07.      STRAND SORT (33.83931 seconds)
08.   INSERTION SORT (59.93059 seconds)
09.      BUCKET SORT (65.85098 seconds)
10.    EXCHANGE SORT (102.28614 seconds)
11.   SELECTION SORT (104.74053 seconds)
12.    COCKTAIL SORT (123.18565 seconds)
13.      BUBBLE SORT (138.07153 seconds)
14.     PANCAKE SORT (138.13012 seconds)
15.       BRICK SORT (161.36594 seconds)
16.       CYCLE SORT (227.94288 seconds)
17.       GNOME SORT (329.78730 seconds)
```

### Performance Comparison with Small Array, Data Output and All Algorithms

This output was generated with `INITIAL_SIZE=256` and `PRINT_DATA=True` and additional algorithms `slowsort` and `stooge_sort` on Manjaro Linux with i5-1035G1 CPU.

```
= PERFORMANCE COMPARISON

SIZE=256
PRINT_DATA=True

testing brick sort... done (0.00139 seconds)
testing bubble sort... done (0.00160 seconds)
testing bucket sort... done (0.00246 seconds)
testing cocktail sort... done (0.00135 seconds)
testing comb sort... done (0.00017 seconds)
testing cycle sort... done (0.00228 seconds)
testing exchange sort... done (0.00115 seconds)
testing gnome sort... done (0.00461 seconds)
testing heap sort... done (0.00035 seconds)
testing insertion sort... done (0.00076 seconds)
testing merge sort... done (0.00030 seconds)
testing pancake sort... done (0.00170 seconds)
testing quicksort... done (0.00028 seconds)
testing selection sort... done (0.00081 seconds)
testing shellsort... done (0.00026 seconds)
testing slowsort... done (128.94381 seconds)
testing stooge sort... done (0.22412 seconds)
testing strand sort... done (0.00043 seconds)
testing tree sort... done (0.00018 seconds)

= RANDOM DATA USED FOR ALL ALGORITHMS

[60889, 10845, 32380, 61269, 60108, 11156, 18823, 34058, 17760, 45486, 16135, 51773, 63704, 1360, 44839, 47412, 29283, 34114, 15323, 10247, 46375, 52281, 63277, 24798, 47869, 39780, 49434, 49796, 64984, 45869, 63345, 39838, 49790, 1316, 39779, 16857, 58389, 38174, 30235, 16331, 55428, 23285, 39343, 36367, 35737, 64720, 51266, 17266, 9756, 47136, 32969, 17941, 34116, 60904, 33666, 57546, 9046, 10411, 34733, 41710, 24077, 50316, 2962, 27222, 8048, 36475, 49423, 14086, 57086, 59065, 54328, 62518, 22289, 21747, 54721, 16585, 35826, 64536, 64132, 14606, 64315, 16781, 34857, 37334, 7539, 41804, 57747, 46654, 56074, 47675, 24220, 23964, 4258, 35107, 52833, 51630, 45669, 19107, 34540, 38549, 41723, 8028, 10383, 51020, 50971, 26443, 61089, 54852, 16471, 45657, 47834, 6827, 4833, 1447, 31089, 8116, 13761, 51299, 16706, 29382, 19064, 27470, 17196, 12174, 23860, 16335, 47470, 13776, 27244, 36304, 28689, 49174, 38437, 26834, 8424, 44419, 65529, 8446, 28351, 20068, 65204, 64934, 56906, 62430, 39607, 7995, 2662, 39459, 7547, 23475, 19408, 7099, 8329, 31054, 62921, 8655, 23174, 60312, 50724, 24874, 32091, 43065, 41533, 29063, 56296, 47773, 54714, 57504, 37774, 46865, 20700, 57932, 53992, 49867, 28613, 32435, 51942, 21520, 49553, 12632, 21033, 38630, 2409, 12104, 2620, 50289, 7388, 39291, 47195, 22812, 62761, 45553, 27864, 12588, 46226, 347, 10902, 8477, 36934, 15279, 22953, 50446, 64452, 1054, 47824, 22017, 1664, 54993, 15458, 22802, 49218, 27201, 37649, 28961, 20020, 59362, 10245, 12321, 5388, 46947, 31146, 12264, 33540, 52858, 20306, 32695, 17271, 17695, 27878, 32786, 36996, 36324, 36756, 804, 58929, 54632, 23405, 47633, 62960, 53004, 65020, 63338, 44453, 48611, 48129, 23213, 15027, 12595, 15145, 20023, 29807, 62536, 34120, 48494, 64277, 49219]

= PERFORMANCE RANKING FOR STATIC DATA

01.        COMB SORT (0.00017 seconds)
02.        TREE SORT (0.00018 seconds)
03.        SHELLSORT (0.00026 seconds)
04.        QUICKSORT (0.00028 seconds)
05.       MERGE SORT (0.00030 seconds)
06.        HEAP SORT (0.00035 seconds)
07.      STRAND SORT (0.00043 seconds)
08.   INSERTION SORT (0.00076 seconds)
09.   SELECTION SORT (0.00081 seconds)
10.    EXCHANGE SORT (0.00115 seconds)
11.    COCKTAIL SORT (0.00135 seconds)
12.       BRICK SORT (0.00139 seconds)
13.      BUBBLE SORT (0.00160 seconds)
14.     PANCAKE SORT (0.00170 seconds)
15.       CYCLE SORT (0.00228 seconds)
16.      BUCKET SORT (0.00246 seconds)
17.       GNOME SORT (0.00461 seconds)
18.      STOOGE SORT (0.22412 seconds)
19.         SLOWSORT (128.94381 seconds)
```
