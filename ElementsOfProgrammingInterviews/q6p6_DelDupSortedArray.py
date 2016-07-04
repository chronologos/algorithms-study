"""
Delete duplicates from a sorted array w/o using lib functions.
O(1) space and O(n) time.
"""

import unittest


class MyTest(unittest.TestCase):
    def test(self):
        a = [1, 1, 2, 2, 4, 5, 5]
        DelDupSortedArray(a)
        self.assertEqual(a, [1, 2, 4, 5])
        pass

    def test2(self):
        a = [1, 1, 2, 2, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5000]
        DelDupSortedArray(a)
        self.assertEqual(a, [1, 2, 4, 5, 5000])
        pass


def DelDupSortedArray(a: list):
    seen_element = None
    vacant_index = 0
    for index, element in enumerate(a):
        if element == seen_element:
            continue
        elif element != seen_element:
            seen_element = element
            a[vacant_index] = element
            vacant_index += 1
    del a[vacant_index:]  # TODO  this is how to trim a list
    return


if __name__ == "__main__":
    unittest.main()
