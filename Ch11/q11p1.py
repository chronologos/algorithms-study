"""

"""
import heapq
import unittest


class MyTest(unittest.TestCase):
    def test(self):
        arrays = [[1,2,3], [], [1,2,4]]
        ans = [1,1,2,2,3,4]
        self.assertEqual(MergeSortedArrays(arrays), ans)


def MergeSortedArrays(arrays):
    heap = []
    res = []
    for index, array in enumerate(arrays):
        if array:
            heapq.heappush(heap, (array.pop(0), index))
    while heap:
        smallest_value, index = heapq.heappop(heap)
        res.append(smallest_value)
        if arrays[index]:
            heapq.heappush(heap, (arrays[index].pop(0), index))
    return res

            

if __name__ == '__main__':
    unittest.main()
