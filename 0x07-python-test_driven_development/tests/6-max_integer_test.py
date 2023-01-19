#!/usr/bin/python3
'''Unittest for max_integer([..])
'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_values(self):
        self.assertIsNone(max_integer([]))

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, 1, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 1, 3, -4]), 3)
