"""
Design an efficient algorithm that takes a sorted array and a key, and finds the index of the first occurence of an element greater than that key.

Outline of Algorithm:
1. binary search for key
2. if M > key: add M to last_index, narrow candidate set
3. if M <= key narrow candidate set
"""

import unittest


class MyTest(unittest.TestCase):
    def test(self):
        a = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        self.assertEqual(modBinSearch(a, 285), 9)
        self.assertEqual(modBinSearch(a, -13), 1)

def modBinSearch(array, key):
    L = 0
    U = len(array)
    last_index = None
    while L <= U:
        M = L + (U - L) / 2
        if array[M] > key:
            last_index = M
            U = M - 1
        elif array[M] <= key:
            L = M + 1
        else:
            raise Error("should never be here")
    return last_index

if __name__ == '__main__':
    unittest.main()
