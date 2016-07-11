"""  
Write a program that takes an integer argument and returns all primes between that integer and 1. 
1 is not prime.
"""
import unittest
import math

class MyTest(unittest.TestCase):


    def test(self):
        a = 25
        self.assertEqual(EnumeratePrimes(a), [2, 3, 5, 7, 11,  13, 17, 19, 23])

    def test2(self):
        def is_prime(num):
            if num == 0 or num == 1:
                return False
            for x in range(2, num):
                if num % x == 0:
                    return False
            else:
                return True
        a = 200
        b = [i for i in range(a) if is_prime(i)]
        self.assertEqual(EnumeratePrimes(200), b)


def EnumeratePrimes(a: int):
    primes = [True for i in range(a+1)]
    is_prime = []
    primes[0:2] = [False, False]  # Set 0 and 1 to not prime
    for i in range(2, a+1):
        if primes[i]:
            is_prime.append(i)
            multiplier = 1
            multiplied_i = multiplier*i
            while multiplied_i <= a:
                #  print ('multiplied_i is %d primes[i] is %d' %(multiplied_i, i))
                primes[multiplied_i] = False
                multiplier += 1
                multiplied_i = multiplier*i
    return is_prime

if __name__ == '__main__':
    unittest.main()
