""" Dutch national flag algorithm


Given array of randomly placed ones, twos and threes,
sort them into [1,1,1,1,...,2,2,2,....3,3,3...] array:
    a[0:lo=0] = 1
    a[lo=0,mid=0] = 2
    a[mid=0,hi=len] unknown
    a[hi=len:len] 3 i.e. to prevent index out of bounds,
    decrement before accessing
"""

# TODO Getting invariants right here was key.
import unittest
import random


class MyTest(unittest.TestCase):

    def setUp(self):
        self.a = [random.randint(1, 3) for i in range(random.randint(10, 40))]
        print (self.a)

    def test(self):
        self.assertEqual(DutchNationalFlag(self.a), sorted(self.a))

    def test2(self):
        self.assertEqual(DutchNationalFlag(self.a), sorted(self.a))

    def test3(self):
        self.assertEqual(DutchNationalFlag(self.a), sorted(self.a))

    def test4(self):
        self.assertEqual(DutchNationalFlag(self.a), sorted(self.a))


def DutchNationalFlag(a: list):
    # [3 2 1]
    PIVOT = 2
    mx = len(a)

    lo = 0
    mid = 0
    hi = mx
    while mid < hi:

        if a[mid] < PIVOT:
            # TODO This is how to exchange variables.
            a[lo], a[mid] = a[mid], a[lo]
            lo += 1
            mid += 1
        elif a[mid] == PIVOT:
            mid += 1
        elif a[mid] > PIVOT:
            hi -= 1
            a[hi], a[mid] = a[mid], a[hi]

    print("lo:{} mid:{} hi:{}".format(lo, mid, hi))
    return a


if __name__ == "__main__":
    unittest.main()
