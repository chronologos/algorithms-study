"""

"""

import unittest


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(BS([1, 2, 3, 4, 5], 3, start=0, end=4), 2)
        self.assertEqual(BS([1, 2, 4, 4, 5], 3, start=0, end=4), -1)
        self.assertEqual(BS([1, 2, 4, 4, 4, 5], 5, start=0, end=5), 5)

def BS (an_array: list, to_find: int, start: int, end: int):
    middle_index = int((start + end)/2)
    if middle_index >= len(an_array):
        return -1
    if an_array[middle_index] == to_find:
        return middle_index
    if start==end:
        return -1
    elif an_array[middle_index] < to_find:
        return BS(an_array, to_find, middle_index, end)
    elif an_array[middle_index] > to_find:
        return BS(an_array, to_find, start, middle_index)
     
    pass

if __name__ == '__main__':
    unittest.main()
