"""
Cyclic check
"""

import unittest
import misc.tree

class MyTest(unittest.TestCase):
    def test(self):
        e = misc.tree.Node(3)       
        d = misc.tree.Node(8, next=e)
        e.next = d
        c = misc.tree.Node(7, next=d)
        b = misc.tree.Node(5, next=c)
        a = misc.tree.Node(2, next=b)
        self.assertTrue(Cyclic(a))
        pass
    def test2(self):
        e = misc.tree.Node(3)       
        d = misc.tree.Node(8, next=e)
        c = misc.tree.Node(7, next=d)
        b = misc.tree.Node(5, next=c)
        a = misc.tree.Node(2, next=b)
        self.assertFalse(Cyclic(a))
        pass
    def test3(self):
        b = misc.tree.Node(5)
        a = misc.tree.Node(2, next=b)
        b.next =  b
        self.assertTrue(Cyclic(a))


def Cyclic(head):
    ptr_fast = head
    ptr_slow = head
    while ptr_fast.next and ptr_slow.next:
        if ptr_fast.next:
            ptr_fast = ptr_fast.next.next
            ptr_slow = ptr_slow.next
            if ptr_fast is ptr_slow:
                return True
        else:
            return False
    return False


if __name__ == '__main__':
    unittest.main()
