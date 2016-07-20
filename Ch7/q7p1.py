"""
Take a string representing an integer and return the corresponding integer.
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(atoi("123"), 123)
        self.assertEqual(atoi("-123"), -123)

    def test2(self):
        self.assertEqual(itoa(123), "123")
        self.assertEqual(itoa(-123), "-123")


def atoi(string: str):
    array = list(string)
    minus = False
    sum = 0
    if array[0] == '-':
        minus = True
        array = array[1:len(array)]
    array.reverse()
    for index, string_number in enumerate(array):
        sum += (10**index) * int(string_number)
    if minus:
        sum = -sum
    return sum


def itoa(integer: int):
    minus = False
    string = ""
    mod = 10
    if integer < 0:
        minus = True
        integer = -integer
    while integer > 0:
        string = str(integer % mod) + string
        integer = integer // 10
    if minus:
        return "-" + string
    else:
        return string


if __name__ == '__main__':
    unittest.main()
