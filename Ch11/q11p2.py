"""
Sort an increasing decreasing array.
"""

import unittest


class MyTest(unittest.TestCase):
    def test(self):
        array = [1,2,3,2,1,2,3]
        res = [[1,2,3], [2,1], [2,3]]
        self.assertEqual(breakIntoSubarrays(array), res)

def someFunc():
    pass
def breakIntoSubarrays(array):
    res = []
    start_index = 0
    increasing = True
    for index, value in enumerate(array):
        print "index %d value %d" %(index, value)
        print res
        if index == 0:
            continue
        elif index == len(array)-1:
            res.append(array[start_index:])
        elif (increasing and array[index-1] > value) or (not increasing and array[index-1] < value):
            print "inside this thing"
            print increasing
            res.append(array[start_index:index])
            start_index = index
            increasing = True if not increasing else False
    return res
if __name__ == '__main__':
    unittest.main()
