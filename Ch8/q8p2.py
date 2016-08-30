"""
Reverse a linked list
"""

import misc.tree
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        c = misc.tree.Node(7)
        b = misc.tree.Node(5, next=c)
        a = misc.tree.Node(2, next=b)
        self.assertEqual(a.Traverse(), [2,5,7])
        Reverse(a)
        self.assertEqual(c.Traverse(), [7,5,2])

    def test2(self):
        a = misc.tree.Node(2)
        Reverse(a)
        self.assertEqual(a.Traverse(), [2])

def OldReverse(head):
    new_tail = head
    temp = new_tail.next
    new_tail.next = None
    new_head = temp

    while new_head:
        temp = new_head.next
        new_head.next = new_tail
        new_tail = new_head
        new_head = temp

def Reverse(head):
    #TODO revise this simple version
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next


if __name__ == '__main__':
    unittest.main()
