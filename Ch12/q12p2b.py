"""
Write a program which takes a sorted array A of integers, and an integer k, and returns the interval enclosing k, i.e., the pair of integers low_bound is the first occurrence of k and high_bound is the last occurrence of k in A. If k does not appear in A, return [None, None].

Algorithm outline:
    1. binary search for k
    2. if k found, set high_bound and low_bound to index(k). then do two modified binary searches. one for k in M + 1 to U and one for k in M - 1 to L. Update high_bound and low_bound accordingly.
    3. else search in other intervals
"""

import unittest


class MyTest(unittest.TestCase):
    def test(self):
        a = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        self.assertEqual(modBinSearch(a, 285), (6,8))

def modBinSearch(array, key):
    L = 0
    U = len(array) - 1
    while L <= U:
        M = L + (U - L) / 2
        if array[M] > key:
            U = M - 1
        elif array[M] < key:
            L = M + 1
        elif array[M] == key:
            high_bound = M
            low_bound = M
            possible_lb = _lbhelper(array, key, L, M - 1)
            if possible_lb: 
                low_bound = possible_lb
            possible_hb = _hbhelper(array, key, M + 1, U)
            if possible_hb:
                high_bound = possible_hb
            return (low_bound, high_bound)
        else:
            return (None, None)

def _lbhelper(subarray, key, L, U):
    candidate_low = None
    while L <= U:
        M = L + (U - L) / 2
        if subarray[M] == key:
            candidate_low = M
            U = M - 1
        else:
            L = M + 1
    return candidate_low

def _hbhelper(subarray, key, L, U):
    candidate_high = None
    while L <= U:
        M = L + (U - L) / 2
        if subarray[M] == key:
            candidate_high = M
            L = M + 1
        else:
            U = M - 1
    return candidate_high

if __name__ == '__main__':
    unittest.main()
