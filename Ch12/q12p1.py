"""
search sorted array for first occurence of k.

1. do binary search for k.

L = 0
U = len(array) - 1
M = L + (U - L) / 2 #NOTE this has a bug where if L is large negative number and U is large positive number we will still get overflow. But when is L large negative number?

2. if found, add k to last_seen_index
3. narrow candidate set down.

with this method complexity bound is still O(log n) because each iteration reduces candidate set by half.
"""

import unittest


class MyTest(unittest.TestCase):
    def test(self):
        a = [-14, -10, 2, 108, 108, 108, 108, 108, 108, 108]
        r = 3
        self.assertEqual(modBinSearch(a, 108), r)


def modBinSearch(array, target):
    L = 0
    U = len(array) - 1
    last_seen_index = None
    while L <= U:
        M = L + (U - L) / 2
        print "L %d, U %d, M %d" %(L, U, M)
        if array[M] > target:
            U = M - 1
        elif array[M] < target:
            L = M + 1
        elif array[M] == target:
            last_seen_index = M
            U = M - 1 # exclude current index out of candidate set
    return last_seen_index



if __name__ == '__main__':
    unittest.main()
