"""
Implement a stack with maximum api
"""

import unittest
# TODO incomplete

class MyTest(unittest.TestCase):
    def test(self):
        stack = Stack()
        stack.push(1)
        stack.push(10)
        stack.push(0)
        self.assertEqual(stack.maximum, 10)
        self.assertEqual(stack.pop(), 0)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.pop(), 1)

        pass

class Stack(object):
    def __init__(self):
        self.array = []
        self.maximum = None
    def push(self, item):
        self.array.append(item)
        if not self.maximum or item > self.maximum:
            self.maximum = item
    def pop(self):
        temp = self.array[len(self.array)-1]
        if temp == self.maximum:
        self.array = self.array[0:len(self.array)-1]
        return temp
        


if __name__ == '__main__':
    unittest.main()
