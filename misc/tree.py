"""
Tree module.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        pass


class TreeNode(object):

    def __init__(self, v, l=None, r=None):
        self.v = v
        if l:
            assert isinstance(l, TreeNode)
        if r:
            assert isinstance(r, TreeNode)
        self.l = l
        self.r = r


class Node(object):

    def __init__(self, v, next=None, prev=None):
        self.v = v
        if next:
            assert isinstance(next, Node)
        if prev:
            assert isinstance(prev, Node)
        self.next = next
        self.prev = prev


def someFunc():
    pass

if __name__ == '__main__':
    unittest.main()
