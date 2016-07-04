"""Optimally buy and sell a stock once given an array of stock prices."""
import unittest


def BuySellStock(a: list):
    minimum = None
    best_min = None
    best_max = None
    max_diff = -1
    for price in a:
        if minimum:
            difference = price - minimum
            if price < minimum:
                minimum = price
            if difference > max_diff:
                max_diff = difference
                best_max = price
                best_min = minimum
        else:
            minimum = price
    return max_diff, best_min, best_max


class MyTest(unittest.TestCase):
    def test(self):
        a = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        self.assertEqual(BuySellStock(a), (30, 260, 290))
        a = [310, 315, 275, 295, 270, 270, 290, 230, 255, 270]
        self.assertEqual(BuySellStock(a), (40, 230, 270))

if __name__ == "__main__":
    unittest.main()
