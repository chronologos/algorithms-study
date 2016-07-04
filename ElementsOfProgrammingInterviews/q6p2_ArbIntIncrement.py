"""

Given an array of digits representing the decimal number D,
increment it to represent the number D + 1.
Must work in languages with limited precision arithmetic as well.

"""

import unittest
import random


class MyTest(unittest.TestCase):

    def setUp(self):
        self.a = [random.randint(7, 9) for i in range(random.randint(10, 40))]
        print (self.a)

    def test(self):
        self.assertEqual(ArbIntIncrement([9, 9, 9, 9]), [1, 0, 0, 0, 0])


def ArbIntIncrement(a: list):
    i = len(a) - 1
    carry = 0
    if a[i] != 9:
        a[i] = a[i] + 1
    else:
        while i >= 0 and a[i] == 9:
            a[i] = 0
            carry = 1
            i -= 1
        if i < 0:
            return [1] + a  # TODO This is how to concatenate lists.
        else:
            a[i] = a[i] + 1
    print (a)
    return a

if __name__ == "__main__":
    unittest.main()
