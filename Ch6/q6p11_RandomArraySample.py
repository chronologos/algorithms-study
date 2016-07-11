"""
Random Array Sample:
Create random subarray of size k from given array in O(1) space and O(k) time.
"""

import unittest


class MyTest(unittest.TestCase):

    def setUp(self):

        class MockRandom(object):
            def __init__(self):
                self.queue = [1, 3, 5, 7, 9]

            def randint(self, unused_min, unused_max):
                return self.queue.pop()

        self.myrandom = MockRandom()

    def test(self):
        self.assertEqual(RandomArraySample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, self.myrandom), [2, 4, 6, 8, 10])



def RandomArraySample(a: list, k: int, r: object):
    for i in range(0, k):
        pick = r.randint(i, len(a)-1)
        print('%d %d', i, pick)
        a[i], a[pick]  = a[pick], a[i]
    return a[0:i]

    return r.randint()

if __name__ == '__main__':
    unittest.main()
