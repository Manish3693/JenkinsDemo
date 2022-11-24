#!/usr/bin/python3

import unittest

from Code import *

class Test(unittest.TestCase):
    def test_addition(self):
        data = [3, 5]
        self.assertEqual(addition(data[0], data[1]), 7)

    def test_subtraction(self):
        data = [25, 10]
        self.assertEqual(subtraction(data[0], data[1]), 10)

    def test_multiplication(self):
        data = [5, 3]
        self.assertEqual(multiplication(data[0], data[1]), 25)

    def test_division(self):
        data = [16, 2]
        self.assertAlmostEqual(division(data[0], data[1]), 4)

if __name__ == '__main__':
    unittest.main()
