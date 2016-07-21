"""
Write a program that takes two linked lists, assumed to be sorted, and returns their merge. The only field your program can change in a node is its next field.
2 -> 5 -> 7
3 -> 8
merge: 2->3->5->7->8
"""
import misc.tree
import unittest


class MyTest(unittest.TestCase):

    def test(self):
        c = misc.tree.Node(7)
        b = misc.tree.Node(5, next=c)
        a = misc.tree.Node(2, next=b)
        d = misc.tree.Node(8)
        e = misc.tree.Node(3, next=d)
        Merge(a, e)
        self.assertEqual(a.Traverse(), [2, 3, 5, 7, 8])
    def testDLL(self):
        c = misc.tree.Node(7)
        b = misc.tree.Node(5, next=c)
        a = misc.tree.Node(2, next=b)
        c.prev = b
        b.prev = a
        d = misc.tree.Node(8)
        e = misc.tree.Node(3, next=d)
        d.prev = e
        MergeDLL(a, e)
        ans = [2, 3, 5, 7, 8]
        self.assertEqual(a.Traverse(), ans)
        ans.reverse()
        self.assertEqual(d.TraverseBack(), ans)


def Merge(node_a, node_b):
    ptr_a = node_a
    ptr_b = node_b
    ptr_new = None

    if not ptr_a:
        return ptr_b
    if not ptr_b:
        return ptr_a
    if ptr_a.v > ptr_b.v:
        ptr_new = ptr_b
        ptr_b = ptr_b.next
    else:
        ptr_new = ptr_a
        ptr_a = ptr_a.next
    ptr_head = ptr_new

    while True:
        if ptr_a and ptr_b:
            if ptr_a.v > ptr_b.v:
                ptr_new.next = ptr_b
                ptr_new = ptr_new.next
                ptr_b = ptr_b.next
            elif ptr_a.v <= ptr_b.v:
                ptr_new.next = ptr_a
                ptr_new = ptr_new.next
                ptr_a = ptr_a.next
        elif ptr_a:
            ptr_new.next = ptr_a
            ptr_new = ptr_new.next
            ptr_a = ptr_a.next

        elif ptr_b:
            ptr_new.next = ptr_b
            ptr_new = ptr_new.next
            ptr_b = ptr_b.next
        else:
            break
    return ptr_head

def MergeDLL(node_a, node_b):
    ptr_a = node_a
    ptr_b = node_b
    ptr_new = None

    if not ptr_a:
        return ptr_b
    if not ptr_b:
        return ptr_a
    if ptr_a.v > ptr_b.v:
        ptr_new = ptr_b
        ptr_b = ptr_b.next
    else:
        ptr_new = ptr_a
        ptr_a = ptr_a.next
    ptr_head = ptr_new

    while True:
        if ptr_a and ptr_b:
            if ptr_a.v > ptr_b.v:
                ptr_new.next = ptr_b
                ptr_b.prev = ptr_new
                ptr_new = ptr_new.next
                ptr_b = ptr_b.next
            elif ptr_a.v <= ptr_b.v:
                ptr_new.next = ptr_a
                ptr_a.prev = ptr_new
                ptr_new = ptr_new.next
                ptr_a = ptr_a.next
        elif ptr_a:
            ptr_new.next = ptr_a
            ptr_a.prev = ptr_new
            ptr_new = ptr_new.next
            ptr_a = ptr_a.next

        elif ptr_b:
            ptr_new.next = ptr_b
            ptr_b.prev = ptr_new
            ptr_new = ptr_new.next
            ptr_b = ptr_b.next
        else:
            break
    return ptr_head



if __name__ == '__main__':
    unittest.main()
