#!/usr/bin/python3

import unittest

from Prog import *

class Test(unittest.TestCase):
    def test_addition(self):
        data = [5, 10]
        self.assertEqual(addition(data[0], data[1]), 15)

    def test_subtraction(self):
        data = [5, 10]
        self.assertEqual(subtraction(data[0], data[1]), -5)

    def test_multiplication(self):
        data = [5, 10]
        self.assertEqual(multiplication(data[0], data[1]), 50)

    def test_division(self):
        data = [16, 2]
        self.assertAlmostEqual(division(data[0], data[1]), 8)

if __name__ == '__main__':
    unittest.main()
