"""
Base conversion. Inputs integer, base1 and base2
Then assume 2<=base1/base2<=16
A for 10, F for 15
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(BaseConvert('2', 10, 2), '10')
        self.assertEqual(BaseConvert('12', 10, 2), '1100')
        self.assertEqual(BaseConvert('15', 10, 16), 'F')
        self.assertEqual(BaseConvert('16', 10, 16), '10')
        self.assertEqual(BaseConvert('255', 10, 16), 'FF')
        self.assertEqual(BaseConvert('16', 10, 10), '16')
        self.assertEqual(BaseConvert('-255', 10, 16), '-FF')
        self.assertEqual(BaseConvert('-255', 10, 16), '-FF')
        self.assertEqual(BaseConvert('222222', 4, 6), '20350')
        self.assertEqual(BaseConvert('222222', 4, 16), 'AAA')
        self.assertEqual(BaseConvert('DEADBEEF', 16, 2), '11011110101011011011111011101111')

DIGITS = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F']


def BaseConvert(number: str, base1: int, base2: int):
    array = list(number)
    minus = False
    if array[0] == '-':
        minus = True
        array = array[1:len(array)]
    number_10 = ToBaseTen(array, base1)  # list to int
    print (number_10)
    number_new = FromBaseTen(number_10, base2)  # int to str
    print (number_new)
    if minus:
        return "-" + number_new
    return number_new


def ToBaseTen(number: list, base_in: int):
    """number is a list of strings"""
    number_10 = 0
    number.reverse()
    for index, str_digit in enumerate(number):
        number_10 = number_10 + DIGITS.index(str_digit) * (base_in**index)
    return number_10


def FromBaseTen(number: int, base_out: int):
    number_new = ""
    while number > 0:
        number_new = DIGITS[number % base_out] + number_new
        number = number // base_out
    return number_new


if __name__ == '__main__':
    unittest.main()
