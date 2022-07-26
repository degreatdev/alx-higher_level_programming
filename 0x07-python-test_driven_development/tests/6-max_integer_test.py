#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer_int(self):
        list = [3, 8, 0, 9, 7]
        self.assertEqual(max_integer(list), 9)

    def test_max_integer_str(self):
        list = ["red", "one", "three"]
        self.assertNotEqual(type(max_integer(list)), int)

    def test_max_integer_none(self):
        list = []
        self.assertIsNone(max_integer(list))

    def test_max_integer_float(self):
        list = [2.4, 5.9, 4.3, 2.3]
        self.assertEqual(max_integer(list), 5.9)

    def test_max_integer_2_max(self):
        list  = [4, 5, 3, 9, 6, 10, 2, 10, 3]
        self.assertEqual(max_integer(list), 10)

    def test_max_integer_mixType(self):
        list = [3, 22.8, 48, 33.4, 50.9, 50.7, 50.8]
        self.assertEqual(max_integer(list), 50.9)

    def test_max_integer_negative(self):
        list = [-1, -7, -9, -4, -3]
        self.assertEqual(max_integer(list), -1)

    def test_max_integer_negative_float(self):
        list = [-2.8, -3.8, -2.3, -9.0]
        self.assertEqual(max_integer(list), -2.3)
