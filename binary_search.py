"""
Jon Bentley's BinarySearch
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(BinarySearch(a, 5), a.index(5))

    def test2(self):
        a = [-1, -1, -1, -1, -1, -1, -1, -1, -1, 10]
        self.assertEqual(BinarySearch(a, 10), a.index(10))

    def test3(self):
        a = [-1, -1, -1, 4, 5, 6, 7, 8, 9, 100]
        self.assertEqual(BinarySearch(a, 9), a.index(9))

    def test4(self):
        a = [-1, -1, -1, 4, 5, 6, 7, 8, 9, 100]
        self.assertIsNone(BinarySearch(a, 101))

    def test5(self):
        a = [-100, -1, -1, 4, 5, 6, 7, 8, 9, 100]
        self.assertIn(BinarySearch(a, -1), [1, 2])


def BinarySearch(a: list, to_find: int):
    l = 0
    h = len(a) - 1
    while l <= h:
        m = l + (h - l) // 2  # avoid int overflow
        print ("h is %s, l is %s, m is now %s" %(h,l,m))
        if a[m] < to_find:
          l=m + 1
        elif a[m] > to_find:
          h=m - 1
        elif a[m] == to_find:
            print ("found m: %s" % m)
            return m
    return None

if __name__ == '__main__':
    unittest.main()
