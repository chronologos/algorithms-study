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

    def Traverse(self):
        ptr = self
        ret = [self.v]
        while ptr.next:
            ptr = ptr.next
            ret.append(ptr.v)
        return ret

    def TraverseBack(self):
        ptr = self
        ret = [self.v]
        while ptr.prev:
            ptr = ptr.prev
            ret.append(ptr.v)
        return ret

def someFunc():
    pass

if __name__ == '__main__':
    unittest.main()
