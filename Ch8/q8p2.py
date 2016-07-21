"""
Test for cyclicity
"""
import misc
import unittest


class MyTest(unittest.TestCase):
    def test(self):
        e = misc.tree.Node(3, next=a)
        d = misc.tree.Node(8, next=e)
        c = misc.tree.Node(7, next=d)
        b = misc.tree.Node(5, next=c)
        a = misc.tree.Node(2, next=b)
        self.assertEqual(Cyclic(a), True)
    def test2(self):
        e = misc.tree.Node(3)
        d = misc.tree.Node(8, next=e)
        c = misc.tree.Node(7, next=d)
        b = misc.tree.Node(5, next=c)
        a = misc.tree.Node(2, next=b)
        self.assertEqual(Cyclic(a), False)
    def test3(self):
        e = misc.tree.Node(3, next=d)
        d = misc.tree.Node(8, next=e)
        c = misc.tree.Node(7, next=d)
        b = misc.tree.Node(5, next=c)
        a = misc.tree.Node(2, next=b)
        self.assertEqual(Cyclic(a), True)

def Cyclic(node):
    ptr_slow = node
    ptr_fast = node
    if ptr_fast.next.next and ptr_slow.next:


if __name__ == '__main__':
    unittest.main()
