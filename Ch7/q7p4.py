"""
Replace and remove from list of chars. Each a is replaced by two ds. Each entry with a b is deleted.
"""

import unittest
import collections

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(ReplaceRemove(['a','c','d','b','b','c','a']),['d','d','c','d','c','d','d'])


def ReplaceRemove(a:list):
    r = []
    for item in a:
        if item == 'a':
            r.append('d')
            r.append('d')
        elif item == 'b':
            continue
        else:
            r.append(item)
    return r



if __name__ == '__main__':
    unittest.main()
