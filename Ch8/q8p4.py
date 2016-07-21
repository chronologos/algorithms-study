"""
Cyclic check
"""

import unittest
import misc.tree

class MyTest(unittest.TestCase):
    def test(self):
        e = misc.tree.Node(3, next=d)       
        d = misc.tree.Node(8, next=e)
        c = misc.tree.Node(7, next=d)
        b = misc.tree.Node(5, next=c)
        a = misc.tree.Node(2, next=b)
        self.assert(Cyclic(a), True)
        pass


def Cyclic(head):
    ptr_fast = head
    ptr_slow = head
    while ptr_fast.next.next and ptr_slow.next:
        ptr_fast = ptr_fast.next.next
        ptr_slow = ptr_slow.next
        if ptr_fast is ptr_slow:
            return True
    return False


if __name__ == '__main__':
    unittest.main()
